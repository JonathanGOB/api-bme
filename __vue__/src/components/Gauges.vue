<template>
    <div class="container" style="margin-bottom: 100px; margin-top: 50px">
        <div class="row">
            <div class="col-sm">
                <h1 class="text-center"><small>humidity</small></h1>
                <VueSvgGauge
                        :start-angle="-90"
                        :end-angle="90"
                        :value=humidity
                        :separator-step="5"
                        :min="0"
                        :max="100"
                        :gauge-color="[{ offset: 0, color: '#f54242'}, { offset: 100, color: '#f87979'}]"
                        :scale-interval="0.1"
                />
                <h1 class="text-center"><small>{{humidity}}</small></h1>
            </div>
            <div class="col-sm">
                <h1 class="text-center"><small>temperature</small></h1>
                <VueSvgGauge
                        :start-angle="-90"
                        :end-angle="90"
                        :value=temperature
                        :separator-step="5"
                        :min="0"
                        :max="100"
                        :gauge-color="[{ offset: 0, color: '#f54242'}, { offset: 100, color: '#f87979'}]"
                        :scale-interval="0.1"
                />
                <h1 class="text-center"><small>{{temperature}}</small></h1>
            </div>
            <div class="col-sm">
                <h1 class="text-center"><small>pressure</small></h1>
                <VueSvgGauge
                        :start-angle="-90"
                        :end-angle="90"
                        :value=pressure
                        :separator-step="5"
                        :min="0"
                        :max="100"
                        :gauge-color="[{ offset: 0, color: '#f54242'}, { offset: 100, color: '#f87979'}]"
                        :scale-interval="0.1"
                />
                <h1 class="text-center"><small>{{pressure}}</small></h1>

            </div>
        </div>
    </div>
</template>

<script>
    import {VueSvgGauge} from 'vue-svg-gauge'

    export default {
        name: "Gauges",
        data() {
            return {
                pressure: 0,
                humidity: 0,
                temperature: 0
            }
        },
        components: {
            VueSvgGauge
        },

        methods: {
            changeValues: function (data) {
                // eslint-disable-next-line no-console
                console.log("put your hands up: ", data.data.Data[data.data.Data.length - 1]);
                this.pressure = parseFloat(data.data.Data[data.data.Data.length - 1].pressure);
                this.humidity = parseFloat(data.data.Data[data.data.Data.length - 1].humidity);
                this.temperature = parseFloat(data.data.Data[data.data.Data.length - 1].temperature);
            }
        }
    }
</script>

<style scoped>

</style>