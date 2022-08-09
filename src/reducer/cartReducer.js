import{
    GET_CART,              
    ADD_TO_CART ,         
    DELETE_FROM_CART,      
    CART_LOADING,          
    GET_ITEMS_CART,        
    ADD_ITEMS_TO_CART ,    
    DELETE_ITEMS_FROM_CART,
    CART_ITEM_LOADING             
} from '../types/cartTypes'

const InitialState ={

    cart : [],
    cartItem:[],
    loadingcart:false,
    loadingcartItem:false
}


export const cartReducer = (state = InitialState,action)=>{
    const{type,payload}= action


    switch (type){
        case GET_CART:
           return{
            ...state,
            cart:payload,
            loadingcart:false
           }

        case  ADD_TO_CART :
           return{
            ...state,
            cart:payload,
            loadingcart:false
           }

        case DELETE_FROM_CART:
            return{
                ...state,
                cart:payload,
                loadingcart:false
               }
           
        case CART_LOADING:
            return{
                ...state,
                loadingcart:true
               }

        case GET_ITEMS_CART:
            return{
                ...state,
                cartItem:payload,
                loadingcartItem:false
               }
           
        case ADD_ITEMS_TO_CART :
            return{
                ...state,
                loadingcartItem:false
               }

        case DELETE_ITEMS_FROM_CART:
            return{
                ...state,
                loadingcartItem:false
               }

        case CART_ITEM_LOADING :
            localStorage.removeItem('token')
            return{
                ...state,
                loadingcartItem:true
               }

        default:
           return state;

            

    }
}