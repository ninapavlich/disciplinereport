// NAME: 
//      SaveLayers

// DESCRIPTION: 
//      Creates a css stylesheet which contains various types of markup for each layer that doesn't start with an underscore
//      It also generates a normal and double-sized imaged
//      TODO: Implement before, after above, below binding for icon_block mixin
//      TODO: Implement before, after above, below binding for has_icon mixin
//      TODO: Verify padding on all sides for icon_block mixin
//      TODO: Verify padding on all sides for has_icon mixin
// REQUIRES: 
//      Adobe Photoshop CS2 or higher
// VERSIONS:
//      21 Jan 2014 by Nina Pavlich
//              Change script functionality to automate exporting sprite sheets for use with SASS


#target photoshop
app.bringToFront();

function main() {
    //SETTINGS:
    var css_image_path = "../img/"

    var output_sass_css = true
    var output_sass_mixins = true
    var sass_output_path = "output/icons/"

    var output_css = true
    var css_output_path = "output/css/"

    var output_image = true
    var output_image_path = "output/img/"


    var output_preview = true
    var output_preview_path = "preview/"

    var pad_vertical = 0;
    var pad_horizontal = 0;

    var override_image_path = "https://disciplinereport.s3.amazonaws.com/media/image/icons.png";
    var override_retina_image_path = "https://disciplinereport.s3.amazonaws.com/media/image/icons@2x.png";
    

    // two quick checks
    if(!okDocument()) {
        alert("Document must be saved and be a layered PSD.");
        return; 
    }

    // Define pixels as unit of measurement
    var defaultRulerUnits = preferences.rulerUnits;
    preferences.rulerUnits = Units.PIXELS;

    
    var doc = app.activeDocument;
    var raw_name = getOuputName(doc);    
    var root = app.activeDocument.path;
    var image_path = root + "/"+ output_image_path + raw_name + ".png";
    var retina_image_path = root + "/"+ output_image_path + raw_name + "@2x.png";

    var relative_image_path = css_image_path + raw_name + ".png";
    var relative_retina_image_path = css_image_path + raw_name + "@2x.png";

    var css_image_path = override_image_path==null? relative_image_path : override_image_path;
    var css_retina_image_path = override_retina_image_path==null? relative_retina_image_path : override_retina_image_path;


    //Examine document for elements
    var doc_width = fluffNumber(doc.width);
    var doc_height = fluffNumber(doc.height);
    var activeLayers = getActiveLayers(activeDocument, "");


    if(output_css){
        
        var css_icon_block_path = root + "/"+css_output_path+raw_name+"_icon_block.css";
        var css_has_sprite_path = root + "/"+css_output_path+raw_name+"_has_sprite.css";
        var css_has_icon_path = root + "/"+css_output_path+raw_name+"_has_icon.css";
        var css_media_query_path = root + "/"+css_output_path+raw_name+"_media_query.css";
        var css_all_path = root + "/"+css_output_path+raw_name+".css";

        var icon_block_section = generateIconBlockSection(activeLayers, css_image_path, pad_vertical, pad_horizontal);
        var sprite_section = generateSpriteSection(activeLayers, css_image_path)
        var has_icon_section = generateHasIconSection(activeLayers, css_image_path, pad_vertical, pad_horizontal);
        var media_query_section = getMediaQuerySnippet(css_retina_image_path, doc_width, doc_height);
        var all = icon_block_section + sprite_section + has_icon_section + media_query_section;
        

        saveTxt(icon_block_section, css_icon_block_path);
        saveTxt(sprite_section, css_has_sprite_path);
        saveTxt(has_icon_section, css_has_icon_path);
        saveTxt(media_query_section, css_media_query_path);
        saveTxt(all, css_all_path);
    }

    if(output_sass_css){

        var sass_icon_block_path = root + "/"+sass_output_path+"_"+raw_name+"_icon_block.scss";
        var sass_has_sprite_path = root + "/"+sass_output_path+"_"+raw_name+"_has_sprite.scss";
        var sass_has_icon_path = root + "/"+sass_output_path+"_"+raw_name+"_has_icon.scss";
        var sass_media_query_path = root + "/"+sass_output_path+"_"+raw_name+"_media_query.scss";        
        var sass_all_path = root + "/"+sass_output_path+"_"+raw_name+".scss";        

        var icon_block_section = generateIconBlockSection(activeLayers, css_image_path, pad_vertical, pad_horizontal);
        var sprite_section = generateSpriteSection(activeLayers, css_image_path);
        var has_icon_section = generateHasIconSection(activeLayers, css_image_path, pad_vertical, pad_horizontal);
        var media_query_section = getMediaQuerySnippet(css_retina_image_path, doc_width, doc_height);
        var all = icon_block_section + sprite_section + has_icon_section + media_query_section;

        saveTxt(icon_block_section, sass_icon_block_path);
        saveTxt(sprite_section, sass_has_sprite_path);
        saveTxt(has_icon_section, sass_has_icon_path);
        saveTxt(media_query_section, sass_media_query_path);
        saveTxt(all, sass_all_path);
    }
    

    if(output_sass_mixins){
        var sass_icon_block_path = root + "/"+sass_output_path+"_"+raw_name+"_icon_block_mixins.scss";
        var sass_has_sprite_path = root + "/"+sass_output_path+"_"+raw_name+"_has_sprite_mixins.scss";
        var sass_has_icon_path = root + "/"+sass_output_path+"_"+raw_name+"_has_icon_mixins.scss";
        var sass_media_query_path = root + "/"+sass_output_path+"_"+raw_name+"_media_query_mixins.scss";
        var sass_all_path = root + "/"+sass_output_path+"_"+raw_name+"_mixins.scss";
        
        var icon_block_mixin_section = generateIconBlockMixin(activeLayers, css_image_path, pad_vertical, pad_horizontal);
        var sprite_mixin_section = generateSpriteMixin(activeLayers, css_image_path);
        var has_icon_mixin_section = generateHasIconMixin(activeLayers, css_image_path, pad_vertical, pad_horizontal);
        var media_query_mixin_section = getMediaQueryMixin(css_retina_image_path, doc_width, doc_height);
        var mixins_all = icon_block_mixin_section + sprite_mixin_section + has_icon_mixin_section + media_query_mixin_section;

        saveTxt(icon_block_mixin_section, sass_icon_block_path);
        saveTxt(sprite_mixin_section, sass_has_sprite_path);
        saveTxt(has_icon_mixin_section, sass_has_icon_path);
        saveTxt(media_query_mixin_section, sass_media_query_path);
        saveTxt(mixins_all, sass_all_path);
    }
    
    
    if(output_image){

        //Resize to half size and save out
        doc.resizeImage(null,UnitValue("200","%"),null,ResampleMethod.BICUBICSMOOTHER);
        SavePNG( File( retina_image_path ) );
        
        //Return to original size.
        doc.resizeImage(null,UnitValue("50","%"),null,ResampleMethod.BICUBICSHARPER);
        SavePNG( File( image_path ) );

    }

    if(output_preview){

        var preview_image_path = root + "/"+ output_preview_path + raw_name + ".png";
        var preview_retina_image_path = root + "/"+ output_preview_path + raw_name + "@2x.png";
        var preview_relative_image_path = raw_name + ".png";
        var preview_relative_retina_image_path = raw_name + "@2x.png";
        var preview_html_path = root + "/"+output_preview_path+raw_name+".html";

        //Resize to half size and save out
        doc.resizeImage(null,UnitValue("200","%"),null,ResampleMethod.BICUBICSMOOTHER);
        SavePNG( File( preview_retina_image_path ) );
        
        //Return to original size.
        doc.resizeImage(null,UnitValue("50","%"),null,ResampleMethod.BICUBICSHARPER);
        SavePNG( File( preview_image_path ) );

        
        var css_icon_block_path = root + "/"+output_preview_path+raw_name+"_icon_block.css";
        var css_has_sprite_path = root + "/"+output_preview_path+raw_name+"_has_sprite.css";
        var css_has_icon_path = root + "/"+output_preview_path+raw_name+"_has_icon.css";
        var css_media_query_path = root + "/"+output_preview_path+raw_name+"_media_query.css";

        saveTxt(generateIconBlockSection(activeLayers, preview_relative_image_path, pad_vertical, pad_horizontal), css_icon_block_path);
        saveTxt(generateSpriteSection(activeLayers, preview_relative_image_path), css_has_sprite_path);
        saveTxt(generateHasIconSection(activeLayers, preview_relative_image_path, pad_vertical, pad_horizontal), css_has_icon_path);
        saveTxt(getMediaQuerySnippet(preview_relative_retina_image_path, doc_width, doc_height), css_media_query_path);

        var html_output = generateHTMLExample(activeLayers, raw_name+"_icon_block.css", raw_name+"_has_sprite.css", raw_name+"_has_icon.css", raw_name+"_media_query.css")
        saveTxt(html_output, preview_html_path);
    }
    
    alert("Done generating sprite and styles for "+activeLayers.length+" icons.") 
    //alert("Done generating sprite sheet. "+activeLayers.length+" sprites were mapped.")
}
function getActiveLayers(parent_layer, name_prefix, output){
    var len = parent_layer.layers.length;
    if(typeof(output)=="undefined"){
        output = [];
    }
    
    for (var i = 0; i < len; i++) {
        var layer = parent_layer.layers[i];
        var layer_name = layer.name;

        if(layer_name.charAt(0) != "_"){

            output.push({
                'name':fluffName(name_prefix+"_"+layer_name),
                'layer':layer,
                'x':getLayerX(layer),
                'y':getLayerY(layer),
                'width':getLayerWidth(layer),
                'height':getLayerHeight(layer)
            }); 

        }else if (layer.typename == 'LayerSet'){
            getActiveLayers(layer, name_prefix+layer_name, output);
        }

    }

    return output;

}

function hideLayers(ref) {
    var len = ref.layers.length;
    for (var i = 0; i < len; i++) {
        var layer = ref.layers[i];
        if (layer.typename == 'LayerSet') hideLayers(layer);
        else layer.visible = false;
    }
}
function getLayerX(layer){
    return fluffNumber(layer.bounds[0]);
}
function getLayerY(layer){
    return fluffNumber(layer.bounds[1]);
}
function getLayerWidth(layer){
    return fluffNumber(layer.bounds[2]) - fluffNumber(layer.bounds[0]);
}
function getLayerHeight(layer){
    return fluffNumber(layer.bounds[3]) - fluffNumber(layer.bounds[1]);
}
function fluffNumber(value){
    var pieces = value.toString().split(" ");
    return parseInt(pieces[0]);
}
function toggleVisibility(ref) {
    var len = ref.layers.length;
    for (var i = 0; i < len; i++) { 
        layer = ref.layers[i];
        layer.visible = !layer.visible;
    }
}

function fluffName(name){
    return name.toLowerCase().replace(/ /g,'_').replace(/[^\w-]+/g,'').slice(1);
}
function getOuputName(doc){
    var pieces = doc.name.split(".");
    pieces.pop();
    return pieces.join(".");
}

function SavePNG(saveFile){
//Pulled from: https://gist.github.com/tomekc/2892034
    
    options = new ExportOptionsSaveForWeb()
    options.quality = 100;  
    options.format = SaveDocumentType.PNG;  
    options.PNG8 = false;
    options.interlaced = false;
    options.transparency = true;

    file = new File( saveFile )
    try{
        app.activeDocument.exportDocument(file, ExportType.SAVEFORWEB, options);    
    }catch(error){
        alert("Error exporting document "+saveFile+": "+error)
    }

}


function saveTxt(txt, filename)
{
    var saveFile = File(filename);

    if(saveFile.exists)
        saveFile.remove();

    saveFile.encoding = "UTF8";
    saveFile.open("e", "TEXT", "????");
    saveFile.writeln(txt);
    saveFile.close();
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

/* CSS TEMPLATES */
function generateCSSContent(items, image, retina_image, w, h, pad_vertical, pad_horizontal){
    return generateIconBlockSection(items, image, pad_vertical, pad_horizontal) + 
    generateSpriteSection(items, image) + 
    generateHasIconSection(items, image, pad_vertical, pad_horizontal,) + 
    getMediaQuerySnippet(retina_image, w, h);
}




function generateIconBlockSection(items, image, pad_vertical, pad_horizontal){
    var output='                                \
/* THIS FILE IS GENREATED by export_icons.js, do not modify - nina@ninalp.com */ \
/* ICON BLOCK STYLE */                          \
.icon_block{                                    \
    position:relative;                          \
    pointer-events:none;                        \
    display:block;                              \
    *zoom: 1;                                   \
}                                               \
.icon_block:before,                             \
.icon_block:after {                             \
    content: " "; /* 1 */                       \
    display: table; /* 2 */                     \
}                                               \
.icon_block:after {                             \
    clear: both;                                \
}                                               \
.icon_block .block{                             \
    display:block;                              \
}                                               \
.icon_block .icon{                              \
    background-image: url("'+image+'");         \
    background-repeat: no-repeat;               \
    display:inline-block;                       \
    text-indent:-9999px;                        \
    float: left;                                \
    position:absolute;                          \
}';

    for each(var item in items){
        var item_bounds = item.layer.bounds;
        //output += 'ITEM NAME: '+item.name+" 0: "+item_bounds[0]+" 1: "+item_bounds[1]+" 2: "+item_bounds[2]+" 3: "+item_bounds[3];
        output+='                               \
.icon_block.'+item.name+' .icon{                \
    background-position: '+(0-item.x)+'px '+(0-item.y)+'px;\
    width: '+item.width+'px;                    \
    height: '+item.height+'px;                  \
}'; 
    }


//Horizontal positioning
for each(var item in items){
output+='                                               \
.icon_block.before.'+item.name+' .icon{                 \
    left: '+(0-item.width)+'px;                         \
}';
output+='                                               \
.icon_block.before.bound_before.'+item.name+' .icon{    \
    left: '+(0)+'px;                                    \
}                                                       \
.icon_block.before.bound_before.'+item.name+' .block{   \
    margin-left: '+(item.width)+'px;                    \
}';

output+='                                               \
.icon_block.left.'+item.name+' .icon{                   \
    margin-left: '+(pad_horizontal)+'px;                \
}';
output+='                                               \
.icon_block.center.'+item.name+' .icon{                 \
    left: 50%;                                          \
    margin-left: -'+((item.width/2)-pad_horizontal)+'px;\
}';
output+='                                               \
.icon_block.right.'+item.name+' .icon{                  \
    right: '+(pad_horizontal)+'px;                      \
}';
output+='                                               \
.icon_block.after.'+item.name+' .icon{                  \
    left: 100%;                                         \
    margin-left: '+(pad_horizontal)+'px;                \
}';
output+='                                               \
.icon_block.after.bound_after.'+item.name+' .icon{      \
    left:initial;                                       \
    left:auto;                                          \
    right: 0px;                                         \
}                                                       \
.icon_block.after.bound_after.'+item.name+' .block{     \
    margin-right: '+(item.width)+'px;                   \
}';

//Vertical positioning
output+='                                               \
.icon_block.above.'+item.name+' .icon{                  \
    top: '+(0-item.height-pad_vertical)+'px;            \
}';
output+='                                               \
.icon_block.above.bound_above.'+item.name+' .icon{      \
    top: '+(0)+'px;                                     \
}                                                       \
.icon_block.above.bound_above.'+item.name+' .block{     \
    margin-top: '+(item.height+pad_vertical)+'px;       \
}';
output+='                                               \
.icon_block.middle.'+item.name+' .icon{                 \
    top: 50%;                                           \
    margin-top: -'+((item.height/2)-pad_vertical)+'px;  \
}';
output+='                                               \
.icon_block.bottom.'+item.name+' .icon{                 \
    top: 100%;                                          \
    margin-top: -'+(item.height+pad_vertical)+'px;      \
}';
output+='                                               \
.icon_block.below.'+item.name+' .icon{                  \
    top: 100%;                                          \
}';
output+='                                               \
.icon_block.below.bound_below.'+item.name+' .icon{      \
    top: initial;                                       \
    top:auto;                                           \
    bottom: '+(0)+'%;                                   \
}                                                       \
.icon_block.below.bound_below.'+item.name+' .block{     \
    margin-bottom: '+(item.height+pad_vertical)+'px;    \
}';
}

    return output;
}
function generateSpriteSection(items, image){
    /* SPRITE SYLE */
    var output ='                                       \
.sprite{                                                \
    background-image: url("'+image+'");                 \
    background-repeat: no-repeat;                       \
    display:inline-block;                               \
    text-indent:-9999px;                                \
}';

    for each(var item in items){
        output+='                                       \
.sprite.'+item.name+'{                                  \
    background-position: '+(0-item.x)+'px '+(0-item.y)+'px;\
    width: '+item.width+'px;                            \
    height: '+item.height+'px;                          \
}';
    }

    return output;
}
function generateHasIconSection(items, image, pad_vertical, pad_horizontal){

    var output ='/* HAS ICON STYLE */                   \
.has_icon{                                              \
    display:block;                                      \
    position:relative;                                  \
}                                                       \
.has_icon:before{                                       \
    content:"";                                         \
    background-image: url("'+image+'");                 \
    background-repeat: no-repeat;                       \
    position:absolute;                                  \
    top: '+pad_vertical+'px;                            \
}';

    for each(var item in items){
        output+='                                       \
.has_icon.'+item.name+':before{                         \
    background-position: '+(0-item.x)+'px '+(0-item.y)+'px;\
    width: '+item.width+'px;                            \
    height: '+item.height+'px;                          \
}';


//Horizontal positioning
output+='                                               \
.has_icon.before.'+item.name+'{                         \
    margin-left: '+(item.width+pad_horizontal)+'px;     \
}                                                       \
.has_icon.before.'+item.name+':before{                  \
    left: '+(0-item.width)+'px;                         \
}';
output+='                                               \
.has_icon.before.bound_before.'+item.name+':before{     \
    left: '+(0)+'px;                                    \
}                                                       \
.has_icon.before.bound_before.'+item.name+'{            \
    padding-left: '+(item.width)+'px;                   \
}';
output+='                                               \
.has_icon.left.'+item.name+':before{                    \
    margin-left: '+(pad_horizontal)+'px;                \
}';
output+='                                               \
.has_icon.center.'+item.name+':before{                  \
    left: 50%;                                          \
    margin-left: -'+((item.width/2)-pad_horizontal)+'px;\
}';
output+='                                               \
.has_icon.right.'+item.name+':before{                   \
    right: '+(pad_horizontal)+'px;                      \
}';
output+='                                               \
.has_icon.after.'+item.name+':before{                   \
    left: 100%;                                         \
    margin-left: '+(pad_horizontal)+'px;                \
}';
output+='                                               \
.has_icon.after.bound_after.'+item.name+':before{       \
    left:initial;                                       \
    left:auto;                                          \
    right: 0px;                                         \
}                                                       \
.has_icon.after.bound_after.'+item.name+'{              \
    padding-right: '+(item.width)+'px;                  \
}';

//Vertical positioning
output+='                                               \
.has_icon.above.'+item.name+':before{                   \
    top: '+(0-item.height-pad_vertical)+'px;            \
}';
output+='                                               \
.has_icon.above.bound_above.'+item.name+':before{       \
    top: '+(0)+'px;                                     \
}                                                       \
.has_icon.above.bound_above.'+item.name+'{              \
    padding-top: '+(item.height+pad_vertical)+'px;      \
}';
output+='                                               \
.has_icon.middle.'+item.name+':before{                  \
    top: 50%;                                           \
    margin-top: -'+((item.height/2)-pad_vertical)+'px;  \
}';
output+='                                               \
.has_icon.bottom.'+item.name+':before{                  \
    top: 100%;                                          \
    margin-top: -'+(item.height+pad_vertical)+'px;      \
}';
output+='                                               \
.has_icon.below.'+item.name+':before{                   \
    top: 100%;                                          \
}';
output+='                                               \
.has_icon.below.bound_below.'+item.name+':before{       \
    top: initial;                                       \
    top:auto;                                           \
    bottom: '+(0)+'%;                                   \
}                                                       \
.has_icon.below.bound_below.'+item.name+'{              \
    padding-bottom: '+(item.height+pad_vertical)+'px;   \
}';

    }
    
    return output;
    
}
function getMediaQuerySnippet(retina_image, width, height){
    return '                                                    \
/* CSS for high-resolution devices */                           \
@media only screen and (-Webkit-min-device-pixel-ratio: 1.5),   \
only screen and (-moz-min-device-pixel-ratio: 1.5),             \
only screen and (-o-min-device-pixel-ratio: 3/2),               \
only screen and (min-device-pixel-ratio: 1.5) {                 \
    .icon_block .icon {                                         \
        background-image: url("'+retina_image+'");              \
        background-size: '+width+'px '+height+'px;              \
        background-repeat: no-repeat;                           \
    }                                                           \
    .has_icon:before{                                           \
        background-image: url("'+retina_image+'");              \
        background-size: '+width+'px '+height+'px;              \
        background-repeat: no-repeat;                           \
    }                                                           \
    .sprite {                                                   \
        background-image: url("'+retina_image+'");              \
        background-size: '+width+'px '+height+'px;              \
        background-repeat: no-repeat;                           \
    }                                                           \
}';
}


function generateIconBlockMixin(items, image, pad_vertical, pad_horizontal){

    var output='                                \
/* THESE MIXINS ARE GENREATED by export_icons.js, do not modify - nina@ninalp.com */ \
@mixin icon_block() {                               \
    position:relative;                              \
    pointer-events:none;                            \
    display:block;                                  \
    *zoom: 1;                                       \
    &:before, &:after{                              \
        content: " "; /* 1 */                       \
        display: table; /* 2 */                     \
    }                                               \
    &:after{                                        \
        clear: both;                                \
    }                                               \
    .block{                                         \
        display:block;                              \
    }                                               \
    .icon{                                          \
        background-image: url("'+image+'");         \
        background-repeat: no-repeat;               \
        display:inline-block;                       \
        text-indent:-9999px;                        \
        float: left;                                \
        position:absolute;                          \
    }                                               \
}                                                   \
@mixin icon_block_debug() {                         \
    border:1px solid #ccc;                          \
    .block{                                         \
        background-color:#ff00ff;                   \
    }                                               \
    .icon{                                          \
        border:1px solid #000;                      \
    }                                               \
}                                                   \
';

    for each(var item in items){
        var item_bounds = item.layer.bounds;
        //output += 'ITEM NAME: '+item.name+" 0: "+item_bounds[0]+" 1: "+item_bounds[1]+" 2: "+item_bounds[2]+" 3: "+item_bounds[3];
        output+='                                                                   \
@mixin icon_block_'+item.name+'($vertical_position:top, $horizontal_position:before, $pad_vertical: '+pad_vertical+', $pad_horizontal: '+pad_horizontal+', $bound_above:true, $bound_after:true, $bound_below:true, $bound_before:true){    \
    @include icon_block();                                                          \
    .block{                                                                         \
        @if $vertical_position == above{                                            \
            @if $bound_above == true{                                               \
                margin-top: ('+(item.height)+'+$pad_vertical)+px;                  \
            }                                                                       \
        }                                                                           \
        @if $vertical_position == below{                                            \
            @if $bound_below == true{                                               \
                margin-bottom: ('+(item.height)+'+$pad_vertical)+px;                \
            }                                                                       \
        }                                                                           \
        @if $horizontal_position == before{                                         \
            @if $bound_before == true{                                              \
                margin-left: ('+(item.width)+'+$pad_horizontal)+px;                 \
            }                                                                       \
        }                                                                           \
        @if $horizontal_position == after{                                          \
            @if $bound_after == true{                                               \
                margin-right: ('+(item.width)+'+$pad_horizontal)+px;                \
            }                                                                       \
        }                                                                           \
    }                                                                               \
    .icon{                                                                          \
        background-position: '+(0-item.x)+'px '+(0-item.y)+'px;                     \
        width: '+item.width+'px;                                                \
        height: '+item.height+'px;                                              \
        @if $horizontal_position == before{                                     \
            @if $bound_before == true{                                          \
                left: '+(0)+'px;                                                \
            }@else{                                                             \
                left: '+(0-item.width)+'px;                                     \
            }                                                                   \
        } @else if $horizontal_position == left {                               \
            margin-left: $pad_horizontal + px;                                  \
        } @else if $horizontal_position == center {                             \
            left: 50%;                                                          \
            margin-left: -('+(item.width/2)+'-$pad_horizontal)+px;              \
        } @else if $horizontal_position == right {                              \
            right: $pad_horizontal + px;                                        \
        } @else if $horizontal_position == after {                              \
            @if $bound_after == true{                                           \
                left:initial;                                                   \
                right: 0px;                                                     \
            }@else{                                                             \
                left: 100%;                                                     \
                margin-left: $pad_horizontal + px;                              \
            }                                                                   \
        }                                                                       \
        @if $vertical_position == above {                                       \
            @if $bound_above == true{                                           \
                top: '+(0)+'px;                                                 \
            }@else{                                                             \
                top: ('+(0-item.height)+'-$pad_vertical)+px;                    \
            }                                                                   \
        } @else if $vertical_position == top {                                  \
            top: $pad_vertical + px;                                            \
        } @else if $vertical_position == middle {                               \
            top: 50%;                                                           \
            margin-top: -('+(item.height/2)+'-$pad_vertical)+px;                \
        } @else if $vertical_position == bottom {                               \
            top: 100%;                                                          \
            margin-top: -('+(item.height)+'+$pad_vertical)+px;                  \
        } @else if $vertical_position == below {                                \
            @if $bound_below == true{                                           \
                top: initial;                                                   \
                bottom: '+(0)+'%;                                               \
            }@else{                                                             \
                top: 100%;                                                      \
            }                                                                   \
        }                                                                       \
    }                                                                           \
}                                                                               \
';


    }

    return output;
}

function generateSpriteMixin(items, image){

    var output ='/* SPRITE STYLE */                 \
@mixin sprite($display: block) {                    \
    background-image: url("'+image+'");             \
    background-repeat: no-repeat;                   \
    display:$display;                               \
    text-indent:-9999px;                            \
}                                                   \
    ';
    
    for each(var item in items){
        output+='                                   \
@mixin sprite_'+item.name+'($display:block, $offset_x:0, $offset_y:0){        \
    @include sprite($display);                      \
    background-position: ('+(0-item.x)+' + $offset_x ) + px ('+(0-item.y)+' + $offset_y ) + px;\
    width: '+item.width+'px;                        \
    height: '+item.height+'px;                      \
}';
    }
        
    return output;

}
function generateHasIconMixin(items, image, pad_vertical, pad_horizontal){
    var output ='/* HAS ICON STYLE */               \
@mixin has_icon() {                                 \
    display: block;                                 \
    position:relative;                              \
    &:before{                                       \
        content:"";                                 \
        background-image: url("'+image+'");         \
        background-repeat: no-repeat;               \
        position:absolute;                          \
    }                                               \
}                                                   \
';
    


    for each(var item in items){
        output+='                                                               \
@mixin has_icon_'+item.name+'($vertical_position:top, $horizontal_position:before, $pad_vertical: '+pad_vertical+', $pad_horizontal: '+pad_horizontal+', $bound_above:true, $bound_after:true, $bound_below:true, $bound_before:true){    \
    @include has_icon();                                                        \
    @if $vertical_position == above{                                            \
        @if $bound_above == true{                                               \
            padding-top:('+(item.height)+'+$pad_vertical)+px;                   \
        }                                                                       \
    }                                                                           \
    @if $vertical_position == below{                                            \
        @if $bound_below == true{                                               \
            padding-bottom: ('+(item.height)+'+$pad_vertical)+px;               \
        }                                                                       \
    }                                                                           \
    @if $horizontal_position == before{                                         \
        @if $bound_before == true{                                              \
            padding-left:('+(item.width)+'+$pad_horizontal)+px;                 \
        }                                                                       \
    }                                                                           \
    @if $horizontal_position == after{                                          \
        @if $bound_after == true{                                               \
            padding-right: ('+(item.width)+'+$pad_horizontal)+px;               \
        }                                                                       \
    }                                                                           \
    &:before{                                                                   \
        background-position: '+(0-item.x)+'px '+(0-item.y)+'px;                 \
        width: '+item.width+'px;                                                \
        height: '+item.height+'px;                                              \
        @if $horizontal_position == before{                                     \
            @if $bound_before == true{                                          \
                left:0px;                                                       \
            }@else{                                                             \
                left: ('+(0-item.width)+'-$pad_horizontal)+px;                  \
            }                                                                   \
        } @else if $horizontal_position == left {                               \
            margin-left: $pad_horizontal+px;                                    \
        } @else if $horizontal_position == center {                             \
            left: 50%;                                                          \
            margin-left: -('+((item.width/2))+'-$pad_horizontal) +px;           \
        } @else if $horizontal_position == right {                              \
            right: 0;                                                           \
            margin-right: $pad_horizontal + px;                                 \
        } @else if $horizontal_position == after {                              \
            @if $bound_after == true{                                           \
                left:initial;                                                   \
                right: 0px;                                    \
            }@else{                                                             \
                left: 100%;                                                     \
                margin-left: $pad_horizontal + px;                              \
            }                                                                   \
        }                                                                       \
        @if $vertical_position == above {                                       \
            @if $bound_above == true{                                           \
                top: '+(0)+'px;                                                 \
            }@else{                                                             \
                top: ('+(0-item.height)+'-$pad_vertical) + px;                  \
            }                                                                   \
        } @else if $vertical_position == top {                                  \
            margin-top: $pad_vertical + px;                                     \
        } @else if $vertical_position == middle {                               \
            top: 50%;                                                           \
            margin-top: -('+((item.height/2))+'-$pad_vertical) + px;            \
        } @else if $vertical_position == bottom {                               \
            top: 100%;                                                          \
            margin-top: -('+(item.height)+'+$pad_vertical)+px;                  \
        } @else if $vertical_position == below {                                \
            @if $bound_below == true{                                           \
                top: initial;                                                   \
                bottom: '+(0)+'%;                                               \
            }@else{                                                             \
                top: 100%;                                                      \
                margin-top: $pad_vertical + px;                                 \
            }                                                                   \
        }                                                                       \
    }                                                                           \
}';
    }
    
    return output;
}

function getMediaQueryMixin(retina_image, width, height){
    return '                                                \
@mixin hi_res() {                                           \
    background-image: url("'+retina_image+'");              \
    background-size: '+width+'px '+height+'px;              \
    background-repeat: no-repeat;                           \
}';
}


function generateHTMLExample(items, css_icon_block_path, css_has_sprite_path, css_has_icon_path, css_media_query_path){
    output='\
    <!DOCTYPE html>\
    <html lang="en" class="no-js">\
    <head>\
        <meta charset="utf-8">\
        <title>Sprite Sheet</title>\
        <meta name="description" content="">\
        <meta name="viewport" content="width=device-width, initial-scale=1">\
        <meta http-equiv="X-UA-Compatible" content="IE=edge">\
        <link rel="stylesheet" href="'+css_icon_block_path+'">\
        <link rel="stylesheet" href="'+css_has_sprite_path+'">\
        <link rel="stylesheet" href="'+css_has_icon_path+'">\
        <link rel="stylesheet" href="'+css_media_query_path+'">\
        <style media="screen" type="text/css">\
            .sprite-showcase .group{\
                margin-bottom:50px;\
            }\
            .sprite-showcase .icon_block,\
            .sprite-showcase .has_icon{\
                border: 1px solid #ccc;\
                margin:150px auto;\
                width:600px;\
            }\
            .sprite-showcase .sprite{\
                margin:5px;\
            }\
        </style>\
    </head>\
    <body>\
        <!-- THIS FILE IS GENREATED by export_icons.js - nina@ninalp.com -->\
        <h1>Sprite Sheet</h1>\
        <div class="main-content-inner">\
             <!-- BEGIN SPRITE SHOWCASE -->\
            <div class="sprite-showcase">\
            <h2>Icons using Simple Sprite method</h2>\
            <p><strong>Usage:</strong> This is the most basic method. This is advised for stand-alone sprites, where a spite is used in place an action -- a play button, next / previous buttons, or list / tile buttons.</p>\
            <div class="group">';


    for each(var item in items){
            output+='\
                    <div class="sprite '+item.name+'">Logo</div>\
            ';
    }
                output+='\
                </div>\
                <h2>Icons using Icon Block method.</h2>\
                <p><strong>Usage:</strong> Use the icon_block method for an icon that is always paired with a piece of text, particularly if is paired with multi-line text.</p>\
                <strong>Note: Only the first few sprites are displayed below, but this layout will work for all sprites displayed in the Simple Sprite method.</strong>\
                <div class="group">';
    var count = Math.min(items.length, 1);
    for (var i=0; i<count;  i++){
        var item = items[i];
            output+='                                       \
                    <div class="icon_block above before '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Above and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block above before bound_before bound_above '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Above and Before - Bound Before and Above</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block above left '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Above and Left</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block above left bound_above '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Above and Left - Bound Above</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block above center '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Above and Center</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block above center bound_above '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Above and Center - Bound Above</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block above right '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Above and Right</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block above right bound_above '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Above and Right - Bound Above</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block above after '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Above and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block above after bound_above bound_after '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Above and After - Bound Above and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block top before '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Top and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block top before bound_before '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Top and Before - Bound Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block top left '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Top and Left</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block top center '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Top and Center</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block top right '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Top and Right</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block top after '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Top and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block top after bound_after '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Top and After - Bound After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block middle before '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Middle and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block middle before bound_before '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Middle and Before - Bound Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block middle left '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Middle and Left</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block middle center '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Middle and Center</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block middle right '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Middle and Right</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block middle after '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Middle and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block middle after bound_after '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Middle and After - Bound After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block bottom before '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Bottom and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block bottom before bound_before '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Bottom and Before - Bound Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block bottom left '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Bottom and Left</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block bottom center '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Bottom and Center</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block bottom right '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Bottom and Right</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block bottom after '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Bottom and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block bottom after bound_after '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Bottom and After - Bound After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block below before '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Below and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block below before bound_before bound_below '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Below and Before - Bound Before and Below</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block below left '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Below and Left</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block below left bound_below '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Below and Left - Bound Below</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block below center '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Below and Center</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block below center bound_below '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Below and Center - Bound Below</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block below right '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Below and Right</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block below right bound_below '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Below and Right - Bound Below</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block below after '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Below and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
                    <div class="icon_block below after bound_below bound_after '+item.name+'">\
                        <div class="icon">Icon</div>\
                        <div class="block">'+item.name+' Icon Block Center <strong>Aligned Below and After - Bound Below and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    </div>\
            ';
    }

                output+='\
            </div>\
                <h2>Icons using Has Icon method. This method uses :before to create generated content. Use ie7.js shim if older ie versions need to be supported.</h2>\
                <p>The has_icon method is elegant because it requires no extra markup. In tradeoff, it is not compatible with older versions of IE where javascript is turned off. This can be used -- but please use only when the icon is not essential to functionality or content.</p>\
                <strong>Note: Only the first few sprites are displayed below, but this layout will work for all sprites displayed in the Simple Sprite method.</strong>\
                <p><strong>Options</strong> Icons can be vertically positioned above, top-aligned, in the middle, bottom-aligned or below the div. The Icon can be horizontally positioned before, left-aligned, centered, right-aligned, or after the div. In addition, you can specify horitzontal and vertical offsets using the sass mixin. If the icon is vertically positioned above or horizontally positioned before, use the bound_above and bound_before arguments to specify whether the icon hangs outside the bounding box or if the entire icon is shifted so that it fits within the bounding box.</p>\
                <div class="group">';

    var count = Math.min(items.length, 1);
    for (var i=0; i<count;  i++){
        var item = items[i];
            output+='\
                    <div class="has_icon above before '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Above and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon above before bound_above bound_before '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Above and Before - Bound Above and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon above left '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Above and Left</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon above left bound_above '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Above and Left - Bound Above</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon above center '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Above and Center</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon above center bound_above '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Above and Center - Bound Above</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon above right '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Above and Right</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon above right bound_above '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Above and Right - Bound Above</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon above after '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Above and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon above after bound_above bound_after '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Above and After - Bound Above and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon top before '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Top and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon top before bound_before '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Top and Before - Bound Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon top left '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Top and Left</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon top center '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Top and Center</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon top right '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Top and Right</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon top after '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Top and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon top after bound_after '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Top and After - Bound After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon middle before '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned middle and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon middle before bound_before '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned middle and Before - Bound Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon middle left '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Middle and Left</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon middle center '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Middle and Center</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon middle right '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Middle and Right</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon middle after '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Middle and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon middle after bound_after '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Middle and After - Bound After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon bottom before '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Bottom and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon bottom before bound_before '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Bottom and Before - Bound Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon bottom left '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Bottom and Left</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon bottom center '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Bottom and Center</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon bottom right '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Bottom and Right</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon bottom after '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Bottom and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon bottom after bound_after '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Bottom and After - Bound After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon below before '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Below and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon below before bound_before bound_below '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Below and Before - Bound Below and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon below left '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Below and Left</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon below left bound_below '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Below and Left - Bound Below</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon below center '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Below and Center</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon below center bound_below '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Below and Center - Bound Below</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon below right '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Below and Right</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon below right bound_below '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Below and Right - Bound Below</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon below after '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Below and After</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <div class="has_icon below after bound_after bound_below '+item.name+'">'+item.name+' Has Icon Method <strong>Aligned Below and After - Bound Below</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</div>\
                    <a href="http://example.com" class="has_icon before top '+item.name+'">'+item.name+' Has Icon Link Method <strong>Aligned Top and Before</strong> Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.</a>\
            ';
    }
                    
                output+='\
                </div>\
            </div>\
        </div>\
    </body>\
</html>';

    return output;
}



wrapper();