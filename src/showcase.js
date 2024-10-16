import nike1 from "./Components/Assets/nike1.png"
import nike2 from "./Components/Assets/nike2.png"
import nike3 from "./Components/Assets/nike3.png"
import nike4 from "./Components/Assets/nike4.png"
import puma1 from "./Components/Assets/puma1.png"
import nb1 from "./Components/Assets/nb1.png"
import nike5 from "./Components/Assets/nike5.png"
import nike6 from "./Components/Assets/nike6.png"
import nike7 from "./Components/Assets/nike7.png"
import adidas1 from "./Components/Assets/adidas1.png"
import nike_f1 from "./Components/Assets/nike_f1.png"
import nike_f2 from "./Components/Assets/nike_f2.png"
import nike_f3 from "./Components/Assets/nike_f3.png"
import on1 from "./Components/Assets/on1.png"

import rebook1 from "./Components/Assets/rebook1.png"
import rebook2 from "./Components/Assets/rebook2.png"

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
]

let men = [
    ...showcase,
    {
        id:5,
        name: "Nike Cortez Leather",
        image:nike2,
        price:90.00,
    },
    {
        id:6,
        name: "VL Court 3.0 Dia de los Muertos",
        image:adidas1,
        price:75.00,
    },
    {
        id:7,
        name: "Nike Air Force 1 '07 High",
        image: nike4,
        price: 103.97,
    },
    {
        id:8,
        name: "Rebook Club C 85",
        image: rebook2,
        price: 75,
    },
    {
        id:9,
        name: "Nike Court Vintage Premium",
        image: nike5,
        price: 68.97,
    },
    {
        id:10,
        name: "Nike Dunk Low Retro",
        image: nike6,
        price: 115,
    },
    {
        id:11,
        name: "Nike P-6000",
        image: nike7,
        price: 110,
    },
]

let women = [
    {
        id:7,
        name: "Nike TC 7900",
        image: nike_f1,
        price: 90.97,
    },
    {
        id:8,
        name: "Reebok x Barbie BB 4000 II",
        image:rebook1,
        price: 100,
    },
    {
        id:10,
        name: "Nike Air Max 270",
        image:nike_f2,
        price: 160,
    },
    {
        id:10,
        name: "Nike Pegasus Plus",
        image:nike_f3,
        price: 180,
    },
    {
        id:10,
        name: "ON Cloud 5",
        image:on1,
        price: 140,
    },
    
]

export { men };
export { women };
export default showcase;