// NAME: 
//      SaveLayers

// DESCRIPTION: 
//      Finds all layers called spacer ane makes them visible
// REQUIRES: 
//      Adobe Photoshop CS2 or higher
// VERSIONS:
//      3 Feb 2014 by Nina Pavlich

#target photoshop
app.bringToFront();

function main() {
       

    // two quick checks
    if(!okDocument()) {
        alert("Document must be saved and be a layered PSD.");
        return; 
    }

    // Define pixels as unit of measurement
    var defaultRulerUnits = preferences.rulerUnits;
    preferences.rulerUnits = Units.PIXELS;

    
    parseLayers(activeDocument);

    alert("DONE")
}
function parseLayers(parent_layer){
    var len = parent_layer.layers.length;
    if(typeof(output)=="undefined"){
        output = [];
    }
    
    for (var i = 0; i < len; i++) {
        var layer = parent_layer.layers[i];
        var layer_name = layer.name;

        if(layer_name.indexOf('_spacer') >=0){
            //Turn layer not visible
            layer.opacity = 0;

        }

        if (layer.typename == 'LayerSet'){
            parseLayers(layer);    
        }
    }

    return output;

}

function okDocument() {
     // check that we have a valid document
     
        if (!documents.length) return false;

        var thisDoc = app.activeDocument; 
        var fileExt = decodeURI(thisDoc.name).replace(/^.*\./,''); 
        return fileExt.toLowerCase() == 'psd'
}

function wrapper() {
    function showError(err) {
        alert(err + ': on line ' + err.line, 'Script Error', true);
    }

    try {
        // suspend history for CS3 or higher
        if (parseInt(version, 10) >= 10) {
                activeDocument.suspendHistory('Save Layers', 'main()');
        } else {
                main();
        }
    } catch(e) {
            // report errors unless the user cancelled
            if (e.number != 8007) showError(e);
    }
}


wrapper();