/** mangular_item.js
 *
 */

var app = angular.module('myApp', ['ngCookies']);

app.controller('custCtrl', function($scope, $http) {

    $scope.myFunc = function() {

        // tworzę pytanie:
        var toSend = {};
        toSend['lookfor'] = $scope.lookfor;
        toSend['category'] = 'item';
        // dodaję csrf:
        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        console.log( 'TX:' + toSend['lookfor']);
        // pytam:
        $http({url: angular_url,
               method: 'POST',
               data: JSON.stringify(toSend),
               }).then(function (response) {
            if (response.data) {
                console.log( 'RX:' + response.data );
                $scope.item_simc_list = response.data;
            }
        });
    }
    angular.element(document).ready(function () {
        $scope.myFunc();
    });
});
