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

  /**
    * TabButton correspond au bouton cliquable qui change le panel
    * TabButton étend de DisclosureButton qui ajoute/enelve l'attribut aria-selected,
    * Et change l'attributte tabindex a 0 si le boutton est actif (value=true), -1 s'il n'est pas actif (value=false)
   */
  var TabButton = /*@__PURE__*/(function (superclass) {
    function TabButton () {
      superclass.call(this, api.core.DisclosureType.SELECT);
    }

    if ( superclass ) TabButton.__proto__ = superclass;
    TabButton.prototype = Object.create( superclass && superclass.prototype );
    TabButton.prototype.constructor = TabButton;

    var staticAccessors = { instanceClassName: { configurable: true } };

    staticAccessors.instanceClassName.get = function () {
      return 'TabButton';
    };

    TabButton.prototype.apply = function apply (value) {
      superclass.prototype.apply.call(this, value);
      if (this.isPrimary) {
        this.setAttribute('tabindex', value ? '0' : '-1');
      }
    };

    Object.defineProperties( TabButton, staticAccessors );

    return TabButton;
  }(api.core.DisclosureButton));

  var TabSelector = {
    TAB: api.ns.selector('tabs__tab'),
    GROUP: api.ns.selector('tabs'),
    PANEL: api.ns.selector('tabs__panel'),
    LIST: api.ns.selector('tabs__list')
  };

  /**
    * Tab coorespond au panel d'un élement Tabs (tab panel)
    * Tab étend disclosure qui ajoute/enleve le modifier --selected,
    * et ajoute/eleve l'attribut hidden, sur le panel
    */
  var TabPanel = /*@__PURE__*/(function (superclass) {
    function TabPanel () {
      superclass.call(this, api.core.DisclosureType.SELECT, TabSelector.PANEL, TabButton, 'TabsGroup');
    }

    if ( superclass ) TabPanel.__proto__ = superclass;
    TabPanel.prototype = Object.create( superclass && superclass.prototype );
    TabPanel.prototype.constructor = TabPanel;

    var staticAccessors = { instanceClassName: { configurable: true } };

    staticAccessors.instanceClassName.get = function () {
      return 'TabPanel';
    };

    TabPanel.prototype.translate = function translate (direction, initial) {
      this.style.transition = initial ? 'none' : '';
      this.style.transform = "translate(" + (direction * 100) + "%)";
    };

    TabPanel.prototype.reset = function reset () {
      this.group.index = 0;
    };

    Object.defineProperties( TabPanel, staticAccessors );

    return TabPanel;
  }(api.core.Disclosure));

  /**
  * TabGroup est la classe étendue de DiscosuresGroup
  * Correspond à un objet Tabs avec plusieurs tab-button & Tab (panel)
  */
  var TabsGroup = /*@__PURE__*/(function (superclass) {
    function TabsGroup () {
      superclass.call(this, 'TabPanel');
    }

    if ( superclass ) TabsGroup.__proto__ = superclass;
    TabsGroup.prototype = Object.create( superclass && superclass.prototype );
    TabsGroup.prototype.constructor = TabsGroup;

    var prototypeAccessors = { buttonHasFocus: { configurable: true } };
    var staticAccessors = { instanceClassName: { configurable: true } };

    staticAccessors.instanceClassName.get = function () {
      return 'TabsGroup';
    };

    TabsGroup.prototype.init = function init () {
      superclass.prototype.init.call(this);
      this.list = this.querySelector(TabSelector.LIST);
      this.listen('transitionend', this.transitionend.bind(this));
      this.listenKey(api.core.KeyCodes.RIGHT, this.pressRight.bind(this), true, true);
      this.listenKey(api.core.KeyCodes.LEFT, this.pressLeft.bind(this), true, true);
      this.listenKey(api.core.KeyCodes.HOME, this.pressHome.bind(this), true, true);
      this.listenKey(api.core.KeyCodes.END, this.pressEnd.bind(this), true, true);

      this.isRendering = true;
    };

    TabsGroup.prototype.transitionend = function transitionend (e) {
      this.style.transition = 'none';
    };

    prototypeAccessors.buttonHasFocus.get = function () {
      return this.members.some(function (member) { return member.buttonHasFocus; });
    };

    /**
     * Selectionne l'element suivant de la liste si on est sur un bouton
     * Si on est à la fin on retourne au début
     */
    TabsGroup.prototype.pressRight = function pressRight () {
      if (this.buttonHasFocus) {
        if (this.index < this.length - 1) {
          this.index++;
        } else {
          this.index = 0;
        }

        this.focus();
      }
    };
    /**
     * Selectionne l'element précédent de la liste si on est sur un bouton
     * Si on est au debut retourne a la fin
     */
    TabsGroup.prototype.pressLeft = function pressLeft () {
      if (this.buttonHasFocus) {
        if (this.index > 0) {
          this.index--;
        } else {
          this.index = this.length - 1;
        }

        this.focus();
      }
    };
    /**
     * Selectionne le permier element de la liste si on est sur un bouton
     */
    TabsGroup.prototype.pressHome = function pressHome () {
      if (this.buttonHasFocus) {
        this.index = 0;
        this.focus();
      }
    };
    /**
     * Selectionne le dernier element de la liste si on est sur un bouton
     */
    TabsGroup.prototype.pressEnd = function pressEnd () {
      if (this.buttonHasFocus) {
        this.index = this.length - 1;
        this.focus();
      }
    };
    TabsGroup.prototype.focus = function focus () {
      if (this.current) { this.current.focus(); }
    };

    TabsGroup.prototype.apply = function apply () {
      for (var i = 0; i < this._index; i++) { this.members[i].translate(-1); }
      this.current.style.transition = '';
      this.current.style.transform = '';
      for (var i$1 = this._index + 1; i$1 < this.length; i$1++) { this.members[i$1].translate(1); }
      this.style.transition = '';
    };

    TabsGroup.prototype.render = function render () {
      if (this.current === null) { return; }
      var paneHeight = Math.round(this.current.node.offsetHeight);
      if (this.panelHeight === paneHeight) { return; }
      this.panelHeight = paneHeight;
      this.style.height = (this.panelHeight + this.list.offsetHeight) + 'px';
    };

    Object.defineProperties( TabsGroup.prototype, prototypeAccessors );
    Object.defineProperties( TabsGroup, staticAccessors );

    return TabsGroup;
  }(api.core.DisclosuresGroup));

  api.tab = {
    TabPanel: TabPanel,
    TabButton: TabButton,
    TabsGroup: TabsGroup,
    TabSelector: TabSelector
  };

  api.register(api.tab.TabSelector.PANEL, api.tab.TabPanel);
  api.register(api.tab.TabSelector.GROUP, api.tab.TabsGroup);

})();
//# sourceMappingURL=tab.nomodule.js.map
