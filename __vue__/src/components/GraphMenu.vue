<template>
    <div>
        <div class="row" >
        <Graph class="col-sm" ref="graph1"/>
        <Settings class="col-sm" @inputs="sendToGraph"></Settings>
        </div>
    </div>
</template>

<script>
    import Graph from "./Graph";
    import axios from "axios";
    import Settings from "./Settings";
    export default {
        name: "GraphMenu",
        components: {Settings, Graph},
        data(){
            return {
                sensor: [],
                deviceId:"",
                handleInterval:""
            }
        },

        methods:{
            sendToGraph: function(value){
                if(this.deviceId != "") {
                    this.$refs.graph1.settings = value;
                    if (value[0].value == true) {
                        this.handleInterval = setInterval(function () {
                            this.getData(this.deviceId)
                        }.bind(this), 1000);
                    }
                    if (value[0].value == false) {
                        clearInterval(this.handleInterval);
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
                            // eslint-disable-next-line no-console
                            console.log(response)
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
                this.$refs.graph1.data = data;
                this.sensor = [];
            }
        },
    }
</script>

<style scoped>

</style>