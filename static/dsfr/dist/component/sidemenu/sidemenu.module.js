/*! DSFR v1.2.1 | SPDX-License-Identifier: MIT | License-Filename: LICENSE.md | restricted use (see terms and conditions) */

const config = {
  prefix: 'fr',
  namespace: 'dsfr',
  organisation: '@gouvfr',
  version: '1.2.1'
};

const api = window[config.namespace];

const SidemenuSelector = {
  LIST: api.ns.selector('sidemenu__list'),
  COLLAPSE: `${api.ns.selector('sidemenu__item')} > ${api.ns.selector('collapse')}`
};

class SidemenuList extends api.core.CollapsesGroup {
  static get instanceClassName () {
    return 'SidemenuList';
  }

  validate (member) {
    return member.node.matches(SidemenuSelector.COLLAPSE);
  }
}

api.sidemenu = {
  SidemenuList: SidemenuList,
  SidemenuSelector: SidemenuSelector
};

api.register(api.sidemenu.SidemenuSelector.LIST, api.sidemenu.SidemenuList);
//# sourceMappingURL=sidemenu.module.js.map
