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
        watch:{
          'data': function () {
              this.fillData();
              // eslint-disable-next-line no-console
              console.log("fill data")
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
                        data.data.map((inner) => {
                            template.data.push(inner.timestamp);
                            template.data.push(inner[element]);
                        })
                        // eslint-disable-next-line no-console
                        console.log("template: ", template);
                        this.datacollection.datasets.push(template);
                    })

                    this.datacollection.labels.push([data.data[0].timestamp, data.data[data.data.length].timestamp]);
                }
            }
        }
    }
</script>

<style>
</style>
