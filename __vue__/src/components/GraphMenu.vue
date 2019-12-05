<template>
    <div>
        <Graph/>
    </div>
</template>

<script>
    import Graph from "./Graph";
    import axios from "axios";
    export default {
        name: "GraphMenu",
        components: {Graph},
        data(){
            return {
                sensor: []
            }
        },

        methods:{
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
            },
        },

    }
</script>

<style scoped>

</style>