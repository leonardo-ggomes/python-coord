/***Mostra e oculta modal */

let modal = document.querySelector(".cal-modal")
let containerModal = document.querySelector(".cal-container-modal")
    
containerModal.addEventListener("click", function(e){
    containerModal.setAttribute("data-cal-show", false)
    containerModal.style.visibility = "hidden"
    
})

modal.addEventListener("click", function(event){
    event.stopPropagation()
})

/*** */
 
 
document.querySelector("#cal-aulas").addEventListener("change", (e) => {
    let caltimeStart = document.getElementById("cal-timeStart")
    let caltimeEnd = document.getElementById("cal-timeEnd")
    let classTime = 45

    if(caltimeStart && caltimeEnd){

        const [hoursStart, minutesStart] = String(caltimeStart.value).split(":")
    
        var d1 = new Date()
        d1.setHours(Number(hoursStart))
        d1.setMinutes(Number(minutesStart)) 
        
        d1.setMinutes(d1.getMinutes() + e.target.value * classTime)


        caltimeEnd.value = String(d1.getHours()).padStart(2,"0") +":"+ String(d1.getMinutes()).padStart(2,"0")

    }     
})

document.querySelector("#cal-timeEnd").addEventListener("blur", (e) => {
    let caltimeStart = document.getElementById("cal-timeStart")
    let calaulas = document.getElementById("cal-aulas")
    let minAula = 45

    if(caltimeStart && calaulas){
        const [hoursStart, minutesStart] = String(caltimeStart.value).split(":")           
        const [hourEnd, minuteEnd] = String(e.target.value).split(":")    
        
        let diferenceHour = Number(hourEnd) - Number(hoursStart)      
        
        let totalAulas = (((diferenceHour * 60) - Number(minutesStart)) + Number(minuteEnd)) / minAula
            
        calaulas.value = Math.round(totalAulas)

    }     
})


document.querySelector("#cal-form").addEventListener("submit", (event) => {
    event.preventDefault()
    getForm()
    event.target.reset()
})



