const weeks = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
const events = document.getElementById("cal-events")

function mountViewEvents() {

    events.innerHTML = ""
 
    for(let c = 0; c < weeks.length; c++){
        const col = document.createElement("div")
        col.id = weeks[c]
        col.classList.add("cal-colDay")

        events.appendChild(col)
    }

    const colhours = document.createElement("div")
    colhours.id = "cal-hours"

    for(let hours = 7; hours < 24; hours++){
        const hour = document.createElement("div")
        let formartHour =  String(hours).padStart(2,"0") + ":00"
        hour.innerText = formartHour
        hour.classList.add("cal-hour")

        hour.addEventListener("click", () => {
            let startTime = document.querySelector("#cal-timeStart")
            startTime.value = formartHour
            
            containerModal.setAttribute("data-cal-show", true)
            containerModal.style.visibility = "visible"
        })
        
        colhours.appendChild(hour)
    }

    events.insertBefore(colhours, document.getElementById(weeks[0]))

}

function loadEvents() {
    mountViewEvents()

    // window.app.receive("onSelectEvent", [""], (data = []) => {
    //     if (data.length > 0) {
    //         data.forEach((dt, index) => {
            
    //             let event = {
    //                 startHourUnformat: dt.start,
    //                 endHourUnformat: dt.end,
    //                 startHourPad: String(dt.start).split(':')[0].padStart(2,"0"),
    //                 startMinutesPad: String(dt.start).split(':')[1].padStart(2,"0"),
    //                 endHourPad: String(dt.end).split(':')[0].padStart(2,"0"),
    //                 endMinutesPad: String(dt.end).split(':')[1].padStart(2,"0"),
    //                 startHours: Number(String(dt.start).split(':')[0]),
    //                 startMinutes: Number(String(dt.start).split(':')[1]),
    //                 endHours: Number(String(dt.end).split(':')[0]),
    //                 endMinutes: Number(String(dt.end).split(':')[1]),
    //                 docente: dt.docente,
    //                 turma: dt.turma,
    //                 etiqueta: dt.etiqueta,
    //                 ambiente: dt.ambiente,
    //                 diaSemana: dt.diasemana,
    //                 codAmbiente: dt.codAmbiente
    //             }
 
    //             let colSemana = document.getElementById(`${event.diaSemana}`)
             
    //             if(colSemana){
    //                 let colAmbiente = document.getElementById(`cal-nc${event.diaSemana}-${event.codAmbiente}`)
    //                 const newEvent = document.createElement("div")
    //                 newEvent.classList.add("cal-event")
    //                 newEvent.style.backgroundColor = event.etiqueta

    //                 let startTop = (event.startHours - 7) * 5.88    
    //                 let startMinTop = event.startMinutes * 0.1
    //                 startTop += startMinTop
    //                 newEvent.style.top = startTop+"%" 

    //                 //Calcula a diferenca de horas
    //                 let horaspx = (event.endHours - event.startHours) * 5.88

    //                 //encontra o percentual dos minutos
    //                 let minutospx = event.endMinutes * 0.1  

    //                 let hmfinal = horaspx + minutospx
    //                 hmfinal -= startMinTop

    //                 newEvent.style.height = "calc("+hmfinal+"%)"                   


    //                 newEvent.innerHTML = `
    //                     <div class="cal-textHour"> ${event.startHourUnformat} - <strong>${event.endHourUnformat}</strong></div>
    //                     <div class="tooltip"> <i class='bx bx-group'> </i>${event.turma}
    //                         <span class="tooltiptext">${event.docente}</span>
    //                     </div>    
    //                 `

    //                 if(colAmbiente) {         
    //                     colAmbiente.appendChild(newEvent)
    //                 }
    //                 else{
    //                     const newColAmbiente = document.createElement("div") 
    //                     newColAmbiente.id = `cal-nc${event.diaSemana}-${event.codAmbiente}`
    //                     newColAmbiente.classList.add("cal-colHour")

    //                     newColAmbiente.appendChild(newEvent)
    //                     colSemana.appendChild(newColAmbiente)   
    //                 }
    //             }

    //         });
    //     }
    // })
}


loadEvents()