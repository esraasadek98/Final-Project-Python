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

import axios from "axiox";

export const getCart=(id)=> async (dispatch)=>{
    dispatch({type , CART_LOADING});
     const config ={
        Heders:{
            'content-type':'aplication/json'
        }
     }
     await axios.get(`${process.env.SERVER_URL}api/cart/${id}/`,config).then((res)=>{
        dispatch({
            type:GET_CART,
            payload:res.data
        })
     })
}

export const addToCart=(id,quantity)=> async (dispatch)=>{
    dispatch({type , CART_LOADING});
     const config ={
        Heders:{
            'content-type':'aplication/json'
        }
     }
     await axios.put(`${process.env.SERVER_URL}api/cart/${id}/`,{ "userid":id , "quantity": quantity +1},config).then((res)=>{
        dispatch({
            type:ADD_TO_CART,
            payload:res.data
        })
     })
} 


export const deleteFromCart=(id,quantity)=> async (dispatch)=>{
    dispatch({type , CART_LOADING});
     const config ={
        Heders:{
            'content-type':'aplication/json'
        }
     }
     await axios.put(`${process.env.SERVER_URL}api/cart/${id}/`,{"userid":id, "quantity": quantity-1},config).then((res)=>{
        dispatch({
            type:DELETE_FROM_CART,
            payload:res.data
        })
     })
} 



export const getItemsCart=(cartId)=> async (dispatch)=>{
    dispatch({type , CART_LOADING});
     const config ={
        Heders:{
            'content-type':'aplication/json'
        }
     }
     await axios.get(`${process.env.SERVER_URL}api/showItemCart/${cartId}/`,{"userid":id, "quantity": quantity-1},config).then((res)=>{
        dispatch({
            type:DELETE_FROM_CART,
            payload:res.data
        })
     })
} 



export const addItemToCart=(cartId,productId)=> async (dispatch)=>{
    
     const config ={
        Heders:{
            'content-type':'aplication/json'
        }
     }
     await axios.get(`${process.env.SERVER_URL}api/cartItemDetectSameItem/${productId}/`,config).then((res)=>{

      if (res.data.length === 0){

        await axios.post(`${process.env.SERVER_URL}api/cartItem/`,{"cartId ":cartId,"productId":productId,"quantity":1 },config).then((res2)=>{
           
            dispatch({
                type:ADD_ITEMS_TO_CART,
                payload:res.data
            })
            
        })

      }
      else{
      await axios.put(`${process.env.SERVER_URL}api/cartItem/id/${res.data[0]?.id}`,{"cartId ":carttId,"productId":productId,"quantity":res.data[0]?.quantity + 1 },config)

          }
    })   
    } 



    export const deleteItemFromCart=(id)=> async (dispatch)=>{
        dispatch({type , CART_ITEM_LOADING});
         const config ={
            Heders:{
                'content-type':'aplication/json'
            }
         }
         await axios.delete(`${process.env.SERVER_URL}api/cartItem/${id}/${id}`,{"userid":id, "quantity": quantity-1},config).then((res)=>{
            dispatch({
                type:GET_ITEMS_CART,
                payload:res.data
            })
         })
    } 
    