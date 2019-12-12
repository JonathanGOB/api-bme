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
                sensor: []
            }
        },

        methods:{
            sendToGraph: function(value){
                this.$refs.graph1.settings = value
            },

            getData: function(device_id){
                device_id = "'" + device_id + "'"
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