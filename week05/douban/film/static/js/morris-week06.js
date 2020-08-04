$(function() {
    let star_4 = $("#morris-donut-chart").attr('star_4')
    let star_5 = $("#morris-donut-chart").attr('star_5')
    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "四星评论",
            value: star_4
        }, {
            label: "五星评论",
            value: star_5
        }],
        resize: true
    });


});
