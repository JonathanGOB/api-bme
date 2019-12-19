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
                localSettings: null,
                localData: null
            }
        },


        methods: {
            fillData (data) {
                let start = false;
                this.localSettings = [];
                this.localData = {
                    "date from": null,
                    "date to": null
                };
                this.settings.map((element) => {
                    if(element.value && element.text != "live" && element.text != "date from" && element.text != "date to"){
                        this.localSettings.push(element.text)
                    }
                    else if(element.text == "date from" || element.text == "date to"){
                        this.localData[element.text] = element.value;
                    }
                });

                // eslint-disable-next-line no-console
                console.log("date ", this.localData['date from'])

                //sorts data
                let methodData = data.sort(function(a,b){
                    return new Date(a.timestamp) - new Date(b.timestamp);
                });

                //removes datetime restriction data
                let removers = [];
                for(let i = 0; i < data.length - 1; i++){
                    if((this.localData['date from'] != null && new Date(data[i].timestamp) < new Date(this.localData['date from']))
                        || (this.localData['date to'] != null && new Date(data[i].timestamp) > new Date(this.localData['date to']))){
                        removers.push(i);
                    }
                }

                // eslint-disable-next-line no-console
                console.log("removers", removers)
                for (let i = removers.length; i >= 0; i--)
                    methodData.splice(removers[i],1);

                //empty datacollection to be refilled
                this.datacollection = {
                    labels:[],
                    datasets: [
                    ]
                }

                //puts data in data collection and fills it with filled templates
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
