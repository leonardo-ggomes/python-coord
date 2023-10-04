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

mountViewEvents()



