odoo.define('whatsapp.ControlPanelRenderer', function (require) {
"use strict";
var config = require('web.config');
var data = require('web.data');
var FavoriteMenu = require('web.FavoriteMenu');
var FilterMenu = require('web.FilterMenu');
var GroupByMenu = require('web.GroupByMenu');
var mvc = require('web.mvc');
var SearchBar = require('web.SearchBar');
var TimeRangeMenu = require('web.TimeRangeMenu');

var Renderer = mvc.Renderer;

var ControlPanelController = require('web.ControlPanelRenderer');

// web.ControlPanelModel
ControlPanelController.include({

      _renderSearchBar: function () {
        var oldSearchBar = this.searchBar;
        this.searchBar = new SearchBar(this, {
            context: this.context,
            facets: this.state.facets,
            fields: this.state.fields,
            filterFields: this.state.filterFields,
        });
        var me = this;
        window.mySearchBar = this.searchBar;
        if (window.myContent) {

            return this.searchBar.prependTo(window.myContent).then(
           // return window.myContent.prependTo(this.searchBar).then(
                function () {
            if (oldSearchBar) {
                oldSearchBar.destroy();
            }
            // if (me._searchPanel) {
            //    me.searchBar.appendTo(me._searchPanel);
            // }
        }
            ) ;
        } else {
             console.log(' no  search panel');
              return this.searchBar.appendTo(this.$('.o_searchview')).then(function () {
            if (oldSearchBar) {
                oldSearchBar.destroy();
            }
            // if (me._searchPanel) {
            //    me.searchBar.appendTo(me._searchPanel);
            // }
        });
        }
        return this.searchBar.appendTo(this.$('.o_searchview')).then(function () {
            if (oldSearchBar) {
                oldSearchBar.destroy();
            }

        });
    },

});


});
