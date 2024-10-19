// showcase items
import showcase_1 from "./Components/Assets/Showcase/showcase_1.png"
import showcase_2 from "./Components/Assets/Showcase/showcase_2.png"
import showcase_3 from "./Components/Assets/Showcase/showcase_3.png"
import showcase_4 from "./Components/Assets/Showcase/showcase_4.png"

// men items
import men1 from "./Components/Assets/Men/nike_m1.png"
import men2 from "./Components/Assets/Men/adidas_m1.png"
import men3 from "./Components/Assets/Men/nike_m2.png"
import men4 from "./Components/Assets/Men/rebook_m1.png"
import men5 from "./Components/Assets/Men/nike_m3.png"
import men6 from "./Components/Assets/Men/nike_m4.png"
import men7 from "./Components/Assets/Men/nike_m5.png"

// women items
import women1 from "./Components/Assets/Women/nike_f1.png"
import women2 from "./Components/Assets/Women/rebook_f1.png"
import women3 from "./Components/Assets/Women/nike_f2.png"
import women4 from "./Components/Assets/Women/nike_f3.png"
import women5 from "./Components/Assets/Women/puma_f1.png"
import women6 from "./Components/Assets/Women/puma_f2.png"
import women7 from "./Components/Assets/Women/rebook_f2.png"
import women8 from "./Components/Assets/Women/nike_f4.png"
import women9 from "./Components/Assets/Women/nike_f5.png"

let showcase = [
    {
        id:1,
        name: "Nike Zoom Vomero 5",
        url: "Nike_Zoom_Vomero_5",
        image: showcase_1,
        price: 109.97,
    },
    {
        id:2,
        name: "New Balance 530",
        url: "New_Balance_530",
        image: showcase_2,
        price: 99.99,
    },
    {
        id:3,
        name: "Nike Air Huarache Runner",
        url: "Nike_Air_Huarache_Runner",
        image:showcase_3,
        price:140.00,
    },
    {
        id:4,
        name: "PUMA x LAMELO BALL MB.03",
        url: "PUMAxLAMELO_BALL_MB.03",
        image:showcase_4,
        price:140.00,
    },    
]

let men = [
    ...showcase,
    {
        id:5,
        name: "Nike Cortez Leather",
        url: "Nike_Cortez_Leather",
        image:men1,
        price:90.00,
    },
    {
        id:6,
        name: "VL Court 3.0 Dia de los Muertos",
        url: "VL_Court_3.0_Dia_de_los_Muertos",
        image:men2,
        price:75.00,
    },
    {
        id: 7,
        name: "Nike Air Force 1 '07 High",
        url: "Nike_Air_Force_1_'07_High",
        image: men3,
        price: 103.97,
    },
    {
        id: 8,
        name: "Rebook Club C 85",
        url: "Rebook_Club_C_85",
        image: men4,
        price: 75,
    },
    {
        id: 9,
        name: "Nike Court Vintage Premium",
        url: "Nike_Court_Vintage_Premium",
        image: men5,
        price: 68.97,
    },
    {
        id: 10,
        name: "Nike Dunk Low Retro",
        url: "Nike_Dunk_Low_Retro",
        image: men6,
        price: 115,
    },
    {
        id: 11,
        name: "Nike P-6000",
        url: "Nike_P-6000",
        image: men7,
        price: 110,
    }
]

let women = [
    {
        id: 12,
        name: "Nike TC 7900",
        url: "Nike_TC_7900",
        image: women1,
        price: 90.97,
    },
    {
        id: 13,
        name: "Reebok x Barbie BB 4000 II",
        url: "Reebok_x_Barbie_BB_4000_II",
        image: women2,
        price: 100,
    },
    {
        id: 14,
        name: "Nike Air Max 270",
        url: "Nike_Air_Max_270",
        image: women3,
        price: 160,
    },
    {
        id: 15,
        name: "Nike Pegasus Plus",
        url: "Nike_Pegasus_Plus",
        image: women4,
        price: 180,
    },
    {
        id: 16,
        name: "Puma Palermo Moda Xtra",
        url: "Puma_Palermo_Moda_Xtra",
        image: women5,
        price: 100,
    },
    {
        id: 17,
        name: "Puma STEWIE x TEAM Stewie 3",
        url: "Puma_STEWIE_x_TEAM_Stewie_3",
        image: women6,
        price: 120,
    },
    {
        id: 18,
        name: "Rebook Nano X4",
        url: "Rebook_Nano_X4",
        image: women7,
        price: 112,
    },
    {
        id: 19,
        name: "Nike Air Force 1 Shadow",
        url: "Nike_Air_Force_1_Shadow",
        image: women8,
        price: 114.97,
    },
    {
        id: 20,
        name: "Nike Free Metcon 6",
        url: "Nike_Free_Metcon_6",
        image: women9,
        price: 102.97,
    }
]

export { men };
export { women };
export default showcase;