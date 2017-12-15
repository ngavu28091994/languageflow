window.app.controller('TfidfController', function ($scope, $http) {

    $scope.isFocusItem = function (row, index) {
        return $scope.filterIndex == index && $scope.filterLabel == row["label"];
    };
    $scope.filter = function (text) {
        return _.filter(text, function (item) {
            var expectedClass = item["expected"] == $scope.filterLabel;
            var actualClass = item["actual"] == $scope.filterLabel;
            return expectedClass == $scope.filterExpectedClass && actualClass == $scope.filterActualClass;
        });
    };

    $http.get("tfidf.json")
        .then(function (result) {

            var data = result["data"];
            data = data.slice(0, 100);
            $scope.data = data;
        });
});
