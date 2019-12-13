<template>
    <div>
        <div>
            <line-chart :chart-data="datacollection"></line-chart>
        </div>
    </div>
</template>

<script>
    import LineChart from './LineChart.js'

    export default {
        name: "Graph",
        components: {
            LineChart
        },
        data(){
            return{
                settings:[],
                datacollection: null,
                localSettings: null
            }
        },


        methods: {
            fillData (data) {
                let start = false;
                this.localSettings = [];
                this.settings.map((element) => {
                    if(element.value && element.text != "live" && element.text != "date from" && element.text != "date to"){
                        this.localSettings.push(element.text)
                    }
                });
                let methodData = data.sort(function(a,b){
                    return new Date(a.timestamp) - new Date(b.timestamp);
                });

                this.datacollection = {
                    labels:[],
                    datasets: [
                    ]
                }
                if(this.localSettings.length != 0) {
                    this.localSettings.map((element) => {
                        let template = {
                            label: "",
                            backgroundColor: '#f87979',
                            data: []
                        };
                        template.label = element;
                        methodData.map((inner) => {
                            if(!start){
                                this.datacollection.labels.push(inner.timestamp);
                            }
                            template.data.push(inner[element]);
                        })
                        start = true;
                        this.datacollection.datasets.push(template);
                    })
                }
            }
        }
    }
</script>

<style>
</style>
