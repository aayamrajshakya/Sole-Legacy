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
        description: "The Vomero 5 takes early 2000s running to modern heights. A combination of breathable and durable materials stands ready for the rigors of your day, while Zoom Air cushioning delivers a smooth ride.",
        image: showcase_1,
        price: 109.97,
    },
    {
        id:2,
        name: "New Balance 530",
        url: "New_Balance_530",
        description: "The original MR530 combined turn of the millennium aesthetics with the reliability of a high milage running shoe. The reintroduced 530 applies a contemporary, everyday style outlook to this performance-minded design. A segmented ABZORB midsole is paired with a classic mesh and synthetic overlay upper design, which utilizes sweeping curves and angles for a distinctive, high-tech look.",
        image: showcase_2,
        price: 99.99,
    },
    {
        id:3,
        name: "Nike Air Huarache Runner",
        url: "Nike_Air_Huarache_Runner",
        description: "When it fits this good and looks this great, it doesn’t need a Swoosh logo. The Air Huarache takes on a classic silhouette with a runner-inspired design, mixed materials and rich neutrals for a look that is both nostalgic and brand new. With its stretchy, foot-hugging fabric and futuristic heel cage, it's still everything you love about the Huarache.",
        image: showcase_3,
        price: 140.00,
    },
    {
        id:4,
        name: "PUMA x LAMELO BALL MB.03",
        url: "PUMAxLAMELO_BALL_MB.03",
        description: "Run like an intergalactic MVP in the MB.03 Halloween. NITRO™ foam rockets energy return with each explosive step, while the space-age woven upper lets breathability blast off. Scratch cutouts and slime soles complete the Melo world trip. Get ready for lift-off.",
        image: showcase_4,
        price: 140.00,
    },    
]

let men = [
    ...showcase,
    {
        id:5,
        name: "Nike Cortez Leather",
        url: "Nike_Cortez_Leather",
        description: "You spoke. We listened. Based on your feedback, we've revamped the original Cortez while maintaining the retro appeal you know and love. This version has a wider toe area and firmer side panels, so you can comfortably wear them day in and day out without any warping. Cortez fans—this one’s for you.",
        image: men1,
        price: 90.00,
    },
    {
        id:6,
        name: "Adidas VL Court 3.0 Dia de los Muertos",
        url: "Adidas_VL_Court_3.0_Dia_de_los_Muertos",
        description: "Proudly wear the 3 stripes with the new VL Court 3.0 men's sneakers from the adidas brand. At first glance, they stand out for their leather upper with lace adjustment. It has a vulcanized rubber sole, perfect to wear on the streets or on your skateboard.",
        image: men2,
        price: 75.00,
    },
    {
        id: 7,
        name: "Nike Air Force 1 '07 High",
        url: "Nike_Air_Force_1_'07_High",
        description: "The Air Force 1 High '07 is everything you know best: crisp overlays, bold accents and the perfect amount of flash to let you shine. The padded, high-cut collar with classic hook-and-loop closure adds heritage b-ball comfort while perforations on the toe keep you cool.",
        image: men3,
        price: 103.97,
    },
    {
        id: 8,
        name: "Rebook Club C 85",
        url: "Rebook_Club_C_85",
        description: "Smooth is how you roll. Now, you have the kicks to match. Slip on these Club C 85 sneakers and hit the scene. A simple style means these supple leather shoes pair up with anything. Because sometimes you don't have to say anything to make a statement.",
        image: men4,
        price: 75,
    },
    {
        id: 9,
        name: "Nike Court Vintage Premium",
        url: "Nike_Court_Vintage_Premium",
        description: "The Nike Court Vintage Premium embodies '80s tennis at its best—laid back and stylish. The smooth leather upper combines with micro-branding for a relaxed look and feel while the cushioned sockliner provides smooth comfort with every step.",
        image: men5,
        price: 68.97,
    },
    {
        id: 10,
        name: "Nike Dunk Low Retro",
        url: "Nike_Dunk_Low_Retro",
        description: "Created for the hardwood but taken to the streets, the Nike Dunk Low Retro returns with crisp overlays and original team colors. This basketball icon channels '80s vibes with premium leather in the upper that looks good and breaks in even better. Modern footwear technology helps bring the comfort into the 21st century.",
        image: men6,
        price: 115,
    },
    {
        id: 11,
        name: "Nike P-6000",
        url: "Nike_P-6000",
        description: "The Nike P-6000 draws on the 2006 Nike Air Pegasus, bringing you a mash-up of iconic style that's breathable, comfortable and evocative of that early-2000s vibe.",
        image: men7,
        price: 110,
    }
]

let women = [
    {
        id: 12,
        name: "Nike TC 7900",
        url: "Nike_TC_7900",
        description: "We've taken the look of early 2000s running and made it tough enough for everyday wear. By combining durable materials with soft cushioning, the TC 7900 is ready for your journey.",
        image: women1,
        price: 90.97,
    },
    {
        id: 13,
        name: "Reebok x Barbie BB 4000 II",
        url: "Reebok_x_Barbie_BB_4000_II",
        description: "Girls believe they can do anything. It's time to get the world on board. These kids' court-inspired shoes from Reebok were created in partnership with The Barbie Dream Gap Project. The suede upper features patent leather side stripes and shine mesh accents for a bit of flash.",
        image: women2,
        price: 100,
    },
    {
        id: 14,
        name: "Nike Air Max 270",
        url: "Nike_Air_Max_270",
        description: "Legendary Air gets lifted. Our first lifestyle Air Max brings you comfort, bold style and 270 degrees of Max Air technology to showcase one of our greatest innovations yet. Add a lightweight, airy upper and low-cut collar, and you've got the perfect go-to kicks for everyday fun.",
        image: women3,
        price: 160,
    },
    {
        id: 15,
        name: "Nike Pegasus Plus",
        url: "Nike_Pegasus_Plus",
        description: "Take responsive cushioning to the next level with the Pegasus Plus. It energizes your ride with full-length, superlight ZoomX foam to give you a high level of energy return for everyday runs. And a stretchy Flyknit upper conforms to your foot for a seamless fit.",
        image: women4,
        price: 180,
    },
    {
        id: 16,
        name: "Puma Palermo Moda Xtra",
        url: "Puma_Palermo_Moda_Xtra",
        description: "Straight from our archives, it's the PUMA Palermo. This classic terrace shoe debuted in the 80's and now, we've brought it back for the fans, revitalized as the Palermo Lamoda. With its signature T-toe construction and classic gum sole, this version features a suede upper, synthetic Formstrip, and translucent tooling. Dress it up for something smart casual. Or dress it down for something comfortably chic.",
        image: women5,
        price: 100,
    },
    {
        id: 17,
        name: "Puma STEWIE x TEAM Stewie 3",
        url: "Puma_STEWIE_x_TEAM_Stewie_3",
        description: "Breanna Stewart has won everything there is to win the world of women's basketball. This third edition of her signature shoe is a representation of everything she has accomplished so far and the seeds she has sown for those that follow. It features a woven mesh upper and NITROFOAM™ midsole for responsive power and breathability to dominate the hardwood.",
        image: women6,
        price: 120,
    },
    {
        id: 18,
        name: "Rebook Nano X4",
        url: "Rebook_Nano_X4",
        description: "The Nano X4 Training Shoes are one of the lightest and most breathable Nano iterations yet. These Reebok training shoes are crafted with enhanced stability and support, without excess design features that add weight. The updated Flexweave® woven textile upper is ultralight and a new midfoot ventilation panel allows greater air flow. Ultimate stability comes from the innovative Lift and Run Chassis system, while Floatride Energy Foam cushions every stride.",
        image: women7,
        price: 112,
    },
    {
        id: 19,
        name: "Nike Air Force 1 Shadow",
        url: "Nike_Air_Force_1_Shadow",
        description: "The Nike Air Force 1 Shadow puts a playful twist on a classic b-ball design. Using a layered approach, doubling the branding and exaggerating the midsole, it highlights AF-1 DNA with a bold, new look.",
        image: women8,
        price: 114.97,
    },
    {
        id: 20,
        name: "Nike Free Metcon 6",
        url: "Nike_Free_Metcon_6",
        description: "From power lifts to ladders, from grass blades to grainy platforms, from the turf to the track your workout has a certain purpose, a specific focus. The Free Metcon 6 supports every grunt, growl and “got it!” We added even more forefoot flexibility to our most adaptable trainer and reinforced the heel with extra foam. That means more freedom for dynamic movements during plyos and cardio classes, plus the stable base you need for weights.",
        image: women9,
        price: 102.97,
    }
]

export { men };
export { women };
export default showcase;