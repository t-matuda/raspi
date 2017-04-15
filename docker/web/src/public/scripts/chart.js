var Chart = React.createClass({
  render: function() {
    const config = {
      "chart": {
        "zoomType": "x",
        "type": "spline",
      },
      "title": {"text": ""},
      "xAxis": {
        "type": "datetime",
        "categories": this.state.times, 
      },
      "yAxis": {
        "title": {"text": "Temperature[°C]"}
      }, 
      "series":[{
        "name": "Temperature",
        "data": this.state.values 
      }]
    };
    return (
      <div>
        <h2>現在の室温:{this.state.latest.value} [°C]({this.state.latest.time})</h2>
        <ReactHighcharts config={config} ref="chart"></ReactHighcharts>
      </div>
    );
  },
  getInitialState: function() {
    return {
      times: [],
      values: [],
      latest: {time: '', value:''},
    };
  },
  loadTempsFromServer: function() {
    $.ajax({
      url: "/api/temperatures",
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({times: data.times, values: data.values}); 
      }.bind(this),
      error: function(xhr, status, err) {
        console.error("/api/temperatures", status, err.toString());
      }.bind(this)
    });
  },
  loadLatestFromServer: function() {
    $.ajax({
      url: "/api/latest",
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({latest: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error("/api/latest", status, err.toString());
      }.bind(this)
    });
  },
  componentDidMount: function() {
    this.loadTempsFromServer();
    setInterval(this.loadTempsFromServer, 900000);
    this.loadLatestFromServer();
    setInterval(this.loadLatestFromServer, 900000);
  },
});

ReactDOM.render(
  <Chart />,
  document.getElementById('content')
);
