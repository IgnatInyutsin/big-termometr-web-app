main.controller('index',function($scope,$http,$location,$cookies){
	//контроллер страницы index
	$scope.$parent.pageName = 'index';

	$.ajax({
		url: "http://localhost:82/",
		data: {command: "site-database-pull"},
		success: function(data){
			console.log("a")
		}
	})
});