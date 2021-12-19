var colorPicker = new iro.ColorPicker("#picker", {
    width: 180,
    layout: [
        { 
          component: iro.ui.Box,
          options: {
              layoutDirection: 'horizontal',
          }
        },
        {
        component: iro.ui.Slider,
        options: {
            sliderType: 'hue',
            layoutDirection: 'horizontal',
        }
        }
      ],
})

const values = document.getElementById("color-info")
colorPicker.on(["color:init", "color:change"], function(color){
    values.firstElementChild.innerHTML = "hex : <span>"+color.hexString+"</span>"
    values.lastElementChild.innerHTML = "rgb : <span>"+color.rgbString+"</span>"

})

var rootStyle = document.documentElement.style
colorPicker.on(['color:init', 'color:change'], function(color) {
  rootStyle.setProperty('--iro-color-value', color.rgbString)
})

const rects = document.getElementById("rect-container")

rects.addEventListener("click", function(e){
    const target = e.target
    if(target.className == 'rect'){
        target.style.backgroundColor = colorPicker.color.hexString
        target.innerHTML = colorPicker.color.hexString
    }


})
