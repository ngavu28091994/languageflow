window.app.config(function ($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');
    $stateProvider.state({
        url: '/',
        name: 'result',
        controller: 'ResultController',
        templateUrl: 'web/result/component.html'
    }).state({
        url: '/multilabel',
        name: 'multilabel',
        controller: 'MultiLabelController',
        templateUrl: 'web/multilabel/component.html'
    }).state({
        url: '/multiclass',
        name: 'multiclass',
        controller: 'MultiClassController',
        templateUrl: 'web/multiclass/component.html'
    });
});
