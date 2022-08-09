import {combineReducers} from "redux";
import  {authReducer}     from "./authReducer";
import  {filterReducer}   from "./filterReducer";
import  {cartReducer}     from "./cartReducer";
import  {userReducer}    from "./userReducer";
import  {itemReducer}     from "./itemReducer"

export default combineReducers({
    authReducer,
    filterReducer,
    cartReducer,
    userReducer,
    itemReducer,
}
)
