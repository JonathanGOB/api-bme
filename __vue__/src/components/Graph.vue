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
                // eslint-disable-next-line no-console
                console.log("data: ", data)
                this.localSettings = [];
                this.settings.map((element) => {
                    if(element.value){
                        this.localSettings.push(element.text)
                    }
                });
                // eslint-disable-next-line no-console
                console.log("settings: ", this.localSettings);
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
                        data.map((inner) => {
                            this.datacollection.labels.push(inner.timestamp);
                            template.data.push(inner[element]);
                        })
                        // eslint-disable-next-line no-console
                        console.log("template:", template);
                        this.datacollection.datasets.push(template);
                    })
                }
            }
        }
    }
</script>

<style>
</style>
