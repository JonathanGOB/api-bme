import { Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
    extends: Line,
    mixins: [reactiveProp],
    props: ['chartData', 'options'],
    mounted () {
        // this.chartData is created in the mixin.
        // If you want to pass options please create a local options object
        try {
            this.renderChart(this.chartData, this.options)
        }
        catch (e) {
            // eslint-disable-next-line no-console
            console.log("no data")
        }
    }
}