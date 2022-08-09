import{
    USER_LOADING,   
    USER_LOADED ,    
    AUTH_ERROR,      
    LOGIN_SUCCESS,  
    LOGIN_FAIL,     
    LOGOUT_SUCCESS,  
    REGISTER_SUCCESS,
    REGISTER_FAIL   
} from '../types/auyhTypes'

const InitialState ={

    token: localStorage.getItem('token'),
    IsAuthenticated:null,
    IsLoading:false,
    user:null,
    msg:""
}


export const authReducer = (state = InitialState,action)=>{
    const{type,payload}= action


    switch (type){
        case USER_LOADING:
           return{
            ...state,
            IsLoading:true
           }

        case USER_LOADED:
           return{
            ...state,
            IsLoading:false,
            IsAuthenticated:true,
            user:payload
           }

           case AUTH_ERROR :
           

        case LOGIN_SUCCESS:
            localStorage.setItem('token',JSON.stringify(payload))
           return{
            ...state,
            IsLoading:false,
            IsAuthenticated:true,
            msg:"Login Success"
           }

        case LOGIN_FAIL:
           
        case LOGOUT_SUCCESS:
            localStorage.removeItem('token')
           return{
            ...state,
            token:null,
            IsAuthenticated:false,
            IsLoading:false
           }

        case REGISTER_SUCCESS:
            localStorage.setItem('token',JSON.stringify(payload))
           return{
            ...state,
            IsLoading:false,
            IsAuthenticated:true,
            msg:"Register Success"
           }

        case REGISTER_FAIL:
            localStorage.removeItem('token')
           return{
            ...state,
            token:null,
            IsAuthenticated:false,
            IsLoading:false
           }
        default:
           return state;

            

    }
}