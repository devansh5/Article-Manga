import { combineReducers } from "redux";
import { connectRouter } from "connected-react-router";
import {signupReducer} from "./components/Signup/SignupReducer";
import {loginReducer} from "./components/Login/LoginReducer";
import {articlesReducer} from "./components/Articles/ArticleReducer";
const createRootReducer = history =>
  combineReducers({
    router: connectRouter(history),
    createUser:signupReducer,
    auth:loginReducer,
    articles:articlesReducer,
  });

export default createRootReducer;