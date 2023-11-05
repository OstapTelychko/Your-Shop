document.addEventListener("DOMContentLoaded", function(){
    let first_star = document.querySelector("#first-star")
    let second_star = document.querySelector("#second-star")
    let third_star = document.querySelector("#third-star")
    let fourth_star = document.querySelector("#fourth-star")
    let fifth_star = document.querySelector("#fifth-star")

    let rating_stars = [first_star, second_star, third_star, fourth_star, fifth_star]
    let rate_input = document.querySelector("#id_rating")

    rating_stars.forEach(star =>{
        star.addEventListener("click", function(){
            let rating_value = rating_stars.indexOf(star)+1

            // return to default 
            for (let item of rating_stars){
                if (item.classList.contains("checked")){
                    item.classList.remove("checked")
                }
            }

            // show selected stars
            for (let index of Array(rating_value).keys()){
                rating_stars[index].classList.add("checked")
            }

            rate_input.value = rating_value
        })
    })


    rating_stars.forEach(star =>{
        star.addEventListener("mouseover", function(){
            let rating_value = rating_stars.indexOf(star)+1

            // show stars on mouseover
            for (let index of Array(rating_value).keys()){
                rating_stars[index].classList.add("hover-star")
            }            
        })
    })

    rating_stars.forEach(star =>{
        star.addEventListener("mouseout", function(){
            // let rating_value = rating_stars.indexOf(star)+1

            // return to default 
            for (let item of rating_stars){
                if (item.classList.contains("hover-star")){
                    item.classList.remove("hover-star")
                }
            }
            // // show selected stars
            // for (let index of Array(rating_value).keys()){
            //     rating_stars[index].style.color = "rgb(155, 65, 0)"
            // }
            
            // rate_input.value = rating_value
        })
    })

})