window.app.config(function ($stateProvider, $urlRouterProvider) {
    $urlRouterProvider.otherwise('/');
    $stateProvider.state({
        name: 'multilabel',
        url: '/',
        controller: 'MultiLabelController',
        templateUrl: 'web/multilabel/component.html'
    });
});
