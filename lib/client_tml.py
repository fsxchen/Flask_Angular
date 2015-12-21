html_doc =\
"""
<html ng-app="app">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>ENV Scan</title>
    <link rel="shortcut icon" href="/static/short.ico">
    <link rel="apple-touch-icon" href="/static/fav.png">
    <link rel="stylesheet" href="bower_components/bootstrap/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="css/main.css">

    <script type="text/javascript" src="bower_components/angular/angular.js" charset="utf-8"></script>
    <script type="text/javascript" src="bower_components/jquery/dist/jquery.js" charset="utf-8"></script>
    <script type="text/javascript" src="bower_components/bootstrap/dist/js/bootstrap.min.js"  charset="utf-8"></script>
    <script type="text/javascript" src="bower_components/angular-ui-router/release/angular-ui-router.js" charset="utf-8"></script>
    <script type="text/javascript" src="bower_components/angular-bootstrap/ui-bootstrap-tpls.js"></script>
    <script type="text/javascript" src="bower_components/lodash/lodash.min.js"></script>
    <script type="text/javascript" src="bower_components/restangular/dist/restangular.js"></script>

    <script type="text/javascript" src="js/app.js"></script>
    <script type="text/javascript" src="js/router.js"></script>

</head>

<body>
    <div>
        <div ng-include="'partials/navbar/navbar.html'">

        </div>
    </div>     <!-- end of main -->

    <div ui-view>

    </div>
    <div class="footer">

    </div>
</body>
</html>
"""

app_init_file = \
'''
var app = angular.module('app',[
    'restangular',
//    'app.controllers',
//    'app.services',
//    'app.directives',
//    'app.filters',
//    'ngAnimate',
//    'ngCookies',
    'app.routes',
    'ui.bootstrap'
//    'angular-flash.service',
//    'angular-flash.flash-alert-directive'
]);

app.run(appRun);

app.config(['RestangularProvider', 'flashProvider',
    function(RestangularProvider, flashProvider) {
        flashProvider.errorClassnames.push('alert-danger')
        RestangularProvider.setBaseUrl("http://example.com:9999/v2");
        RestangularProvider.setDefaultHttpFields({cache: true});
}]);

appRun.inject = ['$rootScope', 'loadUser', 'isConfirmed', '$state']

function appRun($rootScope, loadUser, isConfirmed, Restangular, $cookieStore) {
    $rootScope.isHidden = true;
    $rootScope.isAuthenticated = loadUser() ? true : false;
    $rootScope.isConfirmed = isConfirmed()
    $rootScope.$on('$stateChangeStart', function() {
        $rootScope.isAuthenticated = loadUser() ? true : false;
        $rootScope.isConfirmed = isConfirmed()
    })
    Restangular.setDefaultHeaders({
        Authorization: function() {
             return "Token " + $cookieStore.get('token');
             }
        })

    var _curr;

    Object.defineProperty($rootScope,'current',{
       get: function(){
            _curr = _curr ? _curr : loadUser();
            return _curr;
        },
        set: function(val){
            _curr = loadUser();
        }
    });
}

'''

router_init_file = \
'''
var app = angular.module('app.routes',['ui.router']);

app.config(appRouteConfig);

appRouteConfig.$inject = ['$locationProvider', '$stateProvider', '$urlRouterProvider'];

function appRouteConfig($locationProvider, $stateProvider, $urlRouterProvider){
    $locationProvider.html5Mode({
        enablied: true,
        requireBase: false
    });
    $urlRouterProvider.otherwise('index');

    $stateProvider
        .state('index', {
            url:'/index',
            templateUrl: 'partials/main.html',
        })
};
'''
