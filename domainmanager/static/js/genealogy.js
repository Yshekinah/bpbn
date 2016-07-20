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
                                                     { nation: regex },
                                                     { title: regex },
                                                     { headOf: regex });
          myDiagram.highlightCollection(results);
          // try to center the diagram at the first node that was found
          if (results.count > 0) myDiagram.centerRect(results.first().actualBounds);
        }
        myDiagram.commitTransaction("highlight search");
    }

    function theNationFlagConverter(nation) {
      return "https://www.nwoods.com/go/Flags/" + nation.toLowerCase().replace(/\s/g, "-") + "-flag.Png";
    }

    function theInfoTextConverter(info) {
      var str = "";
      if (info.generation) str += "Generation: " + info.generation;
      if (info.headOf) str += "\n\nHead of: " + info.headOf;
      if (typeof info.sire === "number") {
        var bossinfo = myDiagram.model.findNodeDataForKey(info.sire);
        if (bossinfo !== null) {
          str += "\n\nReporting to: " + bossinfo.name;
        }
      }
      return str;
    }