<template>
    <div>
        <div class="row" >
        <Graph style="margin-top: 25px" class="col-sm" ref="graph1"/>
        <Settings class="col-sm" @inputs="sendToGraph" @selected="getData"></Settings>
        </div>
            <Gauge class = "col-sm" ref="gauge">
            </Gauge>
    </div>
</template>

<script>
    import Graph from "./Graph";
    import axios from "axios";
    import Settings from "./Settings";
    import Gauge from "./Gauge";

    export default {
        name: "GraphMenu",
        components: {Settings, Graph, Gauge},
        data(){
            return {
                sensor: [],
                deviceId:"",
                handleInterval:"",
                live: false,
                response: ""
            }
        },

        methods:{
            sendToGraph: function (value) {
                if (this.deviceId !== "") {
                    this.$refs.graph1.settings = value;
                    // eslint-disable-next-line no-console
                    console.log("settings: ", value)
                    value.some(e => {
                            if (!this.live && e.value === true && e.text === "live") {
                                this.handleInterval = setInterval(function () {
                                    this.getData(this.deviceId)
                                }.bind(this), 1000);
                                this.live = true;
                                return true;
                            }
                        }
                    );

                    if (value[0].value === false || value[0].value === "" && this.live) {
                        this.live = false;
                        clearInterval(this.handleInterval);
                        this.getData(this.deviceId);
                    }

                    if (value[0].value === false || value[0].value === "" && !this.live) {
                        this.getData(this.deviceId);
                    }
                }
            }
        ,

            getData: async function(device_id){
                this.deviceId = device_id.replace(/['"]+/g, '');
                await (this.getDeviceData(device_id)).then( ()=> {
                    this.sendData(this.response);
                });
            },

            getDeviceData: function (device_id) {
                return new Promise((resolve, reject)=> {
                    device_id = "'" + device_id + "'"
                        axios.get("http://127.0.0.1:5000/Api/V1/CapturedData?device_id=" + device_id)
                            .then(response => {
                                // JSON responses are automatically parsed.
                                this.response = response
                                resolve(this.response)
                            })
                            .catch(error => {
                                reject(error);
                            })
                    });

            },


            sendData: function () {
                var data = this.response;
                // eslint-disable-next-line no-console
                console.log("length: " , data.length, " Data: ", this.response)
                this.$refs.graph1.fillData(data);
                this.$refs.gauge.updateTable(data);
            }
        },
    }
</script>

<style scoped>

</style>