/*! DSFR v1.2.1 | SPDX-License-Identifier: MIT | License-Filename: LICENSE.md | restricted use (see terms and conditions) */

(function () {
  'use strict';

  var config = {
    prefix: 'fr',
    namespace: 'dsfr',
    organisation: '@gouvfr',
    version: '1.2.1'
  };

  var api = window[config.namespace];

  var SidemenuSelector = {
    LIST: api.ns.selector('sidemenu__list'),
    COLLAPSE: ((api.ns.selector('sidemenu__item')) + " > " + (api.ns.selector('collapse')))
  };

  var SidemenuList = /*@__PURE__*/(function (superclass) {
    function SidemenuList () {
      superclass.apply(this, arguments);
    }

    if ( superclass ) SidemenuList.__proto__ = superclass;
    SidemenuList.prototype = Object.create( superclass && superclass.prototype );
    SidemenuList.prototype.constructor = SidemenuList;

    var staticAccessors = { instanceClassName: { configurable: true } };

    staticAccessors.instanceClassName.get = function () {
      return 'SidemenuList';
    };

    SidemenuList.prototype.validate = function validate (member) {
      return member.node.matches(SidemenuSelector.COLLAPSE);
    };

    Object.defineProperties( SidemenuList, staticAccessors );

    return SidemenuList;
  }(api.core.CollapsesGroup));

  api.sidemenu = {
    SidemenuList: SidemenuList,
    SidemenuSelector: SidemenuSelector
  };

  api.register(api.sidemenu.SidemenuSelector.LIST, api.sidemenu.SidemenuList);

})();
//# sourceMappingURL=sidemenu.nomodule.js.map
