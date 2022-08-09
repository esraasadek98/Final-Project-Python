import{
    FILTER_PRICE,              
    FILTER_RATING,            
    FILTER_CONDITION ,         
    FILTER_PRICE_AND_RATING,   
    FILTER_PRICE_AND_CONDITION,
    FILTER_RATING_AND_CONDITION,
    FILTER_ALL                            
} from '../types/filtersTypes'

import axios from "axiox";

export const filterPrice=(minprice,maxprice)=> async (dispatch)=>{
    
     const config ={
        Heders:{
            'content-type':'aplication/json'
        }
     }
     let url;
     if(minprice && maxprice){
        url =`api/filter/price/${minprice},${maxprice}/`
     }
     else if (minprice && maxprice === ''){
        url =`api/filter/price/min/${minprice}/`
     }
     else {
        url =`api/filter/price/max/${maxprice}/`
     }

     await axios.get(`${process.env.SERVER_URL}${url}/`,config).then((res)=>{
        dispatch({
            type:FILTER_PRICE,
            payload:res.data
        })
     })
}



export const filterRating=(rating)=> async (dispatch)=>{
    
     const config ={
        Heders:{
            'content-type':'aplication/json'
        }
     }
     

     await axios.get(`${process.env.SERVER_URL}api/filter/rating/${rating}/`,config).then((res)=>{
        dispatch({
            type:FILTER_RATING,
            payload:res.data
        })
     })
}


export const filterCondition=(condtion)=> async (dispatch)=>{
    
    const config ={
       Heders:{
           'content-type':'aplication/json'
       }
    }
    

    await axios.get(`${process.env.SERVER_URL}api/filter/condition/${condtion}/`,config).then((res)=>{
       dispatch({
           type:FILTER_CONDITION,
           payload:res.data
       })
    })
}

export const filterPriceAndCondition=(minprice,maxprice,condition)=> async (dispatch)=>{
    
    const config ={
       Heders:{
           'content-type':'aplication/json'
       }
    }
    

    await axios.get(`${process.env.SERVER_URL}api/filter/price_and_condition${minprice}/${maxprice}/${condition}/`,config).then((res)=>{
       dispatch({
           type:FILTER_PRICE_AND_CONDITION,
           payload:res.data
       })
    })
}


export const filterPriceAndRating=(minprice,maxprice,rating)=> async (dispatch)=>{
    
    const config ={
       Heders:{
           'content-type':'aplication/json'
       }
    }
    

    await axios.get(`${process.env.SERVER_URL}api/filter/price_and_rating${minprice}/${maxprice}/${rating}/`,config).then((res)=>{
       dispatch({
           type:FILTER_PRICE_AND_RATING,
           payload:res.data
       })
    })
}



export const filterRatingAndCondition=(rating,condition)=> async (dispatch)=>{
    
    const config ={
       Heders:{
           'content-type':'aplication/json'
       }
    }
    

    await axios.get(`${process.env.SERVER_URL}api/filter/rating_and_condition${rating}/${condition}/`,config).then((res)=>{
       dispatch({
           type:FILTER_RATING_AND_CONDITION,
           payload:res.data
       })
    })
}


export const filterAll=(minprice,maxprice,rating,condition)=> async (dispatch)=>{
    
    const config ={
       Heders:{
           'content-type':'aplication/json'
       }
    }
    

    await axios.get(`${process.env.SERVER_URL}api/filter/rating_and_condition${minprice}/${maxprice}/${rating}/${condition}/`,config).then((res)=>{
       dispatch({
           type:FILTER_ALL,
           payload:res.data
       })
    })
}

