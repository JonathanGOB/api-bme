<template>
    <div>
        <div class="row" >
        <Graph style="margin-top: 25px" class="col-sm" ref="graph1"/>
        <Settings class="col-sm" @inputs="sendToGraph" @selected="getData"></Settings>
        </div>
            <Gauge class = "col-sm" ref="guage">
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
                live:""
            }
        },

        methods:{
            sendToGraph: function(value){
                if(this.deviceId != "") {
                    this.$refs.graph1.settings = value;
                    value.some(e => {
                        if (!this.live && value[0].value == true && e.text != "live" && e.value != "") {
                            this.handleInterval = setInterval(function () {
                                this.getData(this.deviceId)
                            }.bind(this), 1000);
                            this.live = true
                            return true;
                        }
                    }
                );
                    if (value[0].value == false) {
                        this.live = false;
                        clearInterval(this.handleInterval);
                        this.getData(this.deviceId);
                    }
                }
            },

            getData: function(device_id){
                this.deviceId = device_id.replace(/['"]+/g, '');
                device_id = "'" + device_id + "'"
                try {
                    axios.get("http://127.0.0.1:5000/Api/V1/CapturedData?device_id=" + device_id)
                        .then(response => {
                            // JSON responses are automatically parsed.
                            response.data.Data.forEach(CapturedData => this.sensor.push(CapturedData));
                        })
                        .catch(e => {
                            this.errors.push(e)
                        })
                }
                catch (e) {
                    // eslint-disable-next-line no-console
                    console.log()
                }
                this.sendData(this.sensor);
            },

            sendData: function (data) {
                this.$refs.graph1.fillData(data);
                this.$refs.guage.updateTable(data);
                this.sensor = [];
            }
        },
    }
</script>

<style scoped>

</style>