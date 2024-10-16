import nike1 from "./Components/Assets/nike1.png"
import nike2 from "./Components/Assets/nike2.png"
import nike3 from "./Components/Assets/nike3.png"
import nike4 from "./Components/Assets/nike4.png"
import puma1 from "./Components/Assets/puma1.png"
import nb1 from "./Components/Assets/nb1.png"
import adidas1 from "./Components/Assets/adidas1.png"

let showcase = [
    {
        id:1,
        name: "Nike Zoom Vomero 5",
        image:nike1,
        price:109.97,
    },
    {
        id:2,
        name: "New Balance 530",
        image:nb1,
        price:99.99,
    },
    {
        id:3,
        name: "Nike Air Huarache Runner",
        image:nike3,
        price:140.00,
    },
    {
        id:4,
        name: "PUMA x LAMELO BALL MB.03",
        image:puma1,
        price:140.00,
    },
    // {
    //     id:5,
    //     name: "VL Court 3.0 Dia de los Muertos",
    //     image:adidas1,
    //     price:75.00,
    // },
    
]

let nike = [
    ...showcase,
    {
        id:5,
        name: "Nike Cortez Leather",
        image:nike2,
        price:90.00,
    }
]

export { nike };
export default showcase;