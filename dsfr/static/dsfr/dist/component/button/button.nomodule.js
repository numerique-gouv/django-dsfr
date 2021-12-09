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

  var ButtonSelector = {
    EQUISIZED_BUTTON: ((api.ns.selector('btns-group--equisized')) + " " + (api.ns.selector('btn'))),
    EQUISIZED_GROUP: api.ns.selector('btns-group--equisized')
  };

  api.button = {
    ButtonSelector: ButtonSelector
  };

  api.register(api.button.ButtonSelector.EQUISIZED_BUTTON, api.core.Equisized);
  api.register(api.button.ButtonSelector.EQUISIZED_GROUP, api.core.EquisizedsGroup);

})();
//# sourceMappingURL=button.nomodule.js.map
