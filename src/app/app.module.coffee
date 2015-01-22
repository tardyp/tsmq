# first thing, we install underscore.string inside lodash
_.mixin(_.string.exports())

angular.module 'app', [
    'ui.bootstrap'
    'ui.router'
]

angular.module('app').config ($urlRouterProvider, $stateProvider) ->

        state =
            controller: "messagesController"
            templateUrl: "views/messages.html"
            name: 'messages'
            url: '/messages'

        $stateProvider.state(state)

        $urlRouterProvider.otherwise('/messages')
        # all states config are in the modules


class Messages extends Controller
    constructor: ($scope, messages, types) ->
        $scope.messages = messages
        $scope.types = types
