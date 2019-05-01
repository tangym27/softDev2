// Michelle Tang
// SoftDev2 pd6
// K21 -- Onions, Bell Peppers, and Celery, Oh My!  JS and the Holy Trinity
// 2019-04-30

htmlTotal = document.getElementById("total");
htmlPer = document.getElementById("percent");
htmlAvg = document.getElementById("avg");

d3.json("./data.json").then(function(data) {
// first function
    num_students = data.filter(function(n) {
                    return n['schoolyear'] == '20112012'})
        .reduce(function(a, b) {
                    return a + b['total_enrollment']}, 0);
    htmlTotal.innerHTML = num_students + " students!";
// second function
    var total = data.map(
      function(n){
        return parseInt(n["total_enrollment"]);
      }
    );

    num_students=0;
    i=0;
    while(i < total.length){
      num_students+=total[i];
      i++;
    }

    totage=0;
    i=0;
    while(i < total.length){
      totage+=total[i]*i;
      i++;
    }
    mean = totage / num_students
    htmlPer.innerHTML = mean
// third function
    avg = data.filter(function(n) {
                    return n['schoolyear'] == '20112012'})
                .map(function(n) {
                    return parseInt(n['female_per'])})
                .reduce(function(a,b) {
                    return a + b}, 0);

    num_schools = data.filter(function(n) {
                    return n['schoolyear'] == '20112012'})
                .map(function(n) {
                    return parseInt(n['female_per'])});
    htmlAvg.innerHTML = avg/num_schools.length;

});
