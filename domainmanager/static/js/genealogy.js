    // the Search functionality highlights all of the nodes that have at least one data property match a RegExp
    function searchDiagram() {  // called by button
        var input = document.getElementById("mySearch");
        if (!input) return;
        input.focus();
        // create a case insensitive RegExp from what the user typed
        var regex = new RegExp(input.value, "i");
        myDiagram.startTransaction("highlight search");
        myDiagram.clearHighlighteds();
        // search four different data properties for the string, any of which may match for success
        if (input.value) {  // empty string only clears highlighteds collection
          var results = myDiagram.findNodesByExample({ name: regex },
                                                     { clan: regex },
                                                     { title: regex },
                                                     { headOf: regex });
          myDiagram.highlightCollection(results);
          // try to center the diagram at the first node that was found
          if (results.count > 0) myDiagram.centerRect(results.first().actualBounds);
        }
        myDiagram.commitTransaction("highlight search");
    }

    /**
    function theClanConverter(columnStart) {

        var dao;

        switch(true) {
            case columnStart <= 167:
                dao.clan = "Ventrue";
                return dao;
                break;
           case columnStart <= 203:
                return "Salubri";
                break;
           case columnStart <= 254:
                return "Cappadozian";
                break;
           case columnStart <= 363:
                return "Malkavian";
                break;
           case columnStart <= 492:
                return "Brujah";
                break;
           case columnStart <= 526:
                return "Assamite";
                break;
           case columnStart <= 617:
                return "Follower of Set";
                break;
           case columnStart <= 758:
                return "Gangrel";
                break;
           case columnStart <= 795:
                return "Ravnos";
                break;
           case columnStart <= 826:
                return "Tzimisce";
                break;
           case columnStart <= 950:
                return "Nosferatu";
                break;
           case columnStart <= 1110:
                return "Toreador";
                break;
            default:
                return "unknown"
        }
    }
    **/

    function theInfoTextConverter(info) {
      var str = "";
      if (info.clan) str += "\n\nClan: " + info.clan
      if (info.generation) str += "\n\nGeneration: " + info.generation;
      if (info.headOf) str += "\n\nHead of: " + info.headOf;
      if (typeof info.sire === "number") {
        var bossinfo = myDiagram.model.findNodeDataForKey(info.sire);
        if (bossinfo !== null) {
          str += "\n\nReporting to: " + bossinfo.name;
        }
      }
      return str;
    }