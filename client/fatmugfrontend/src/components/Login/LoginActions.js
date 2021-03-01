import axios from "axios";
import {push} from "connected-react-router";
import {toast} from "react-toastify";
import {SET_TOKEN,SET_CURRENT_USER,UNSET_CURRENT_USER} from "./LoginTypes";
import {setAxiosAuthToken,toastOnError} from "../utils/Utils";


export const login=(userData,redirectTo)=>dispatch=>{
    axios.post("api/login/",userData)
    .then(response=>{
        // console.log(response.data.token)
        const auth_token=response.data.token;
        // console.log(response.data);
        setAxiosAuthToken(auth_token);
        dispatch(setToken(auth_token));
        dispatch(getCurrentUser(redirectTo));
    })
    .catch(error=>{
        dispatch(unsetCurrentUser());
        toastOnError(error);
    });
};


export const getCurrentUser=redirectTo=>dispatch=>{
    axios.get("api/login/")
    .then(response=>{
        const user={
            username:response.data.username
        }
        dispatch(setCurrentUser(user,redirectTo));
    })
    .catch(error=>{
        dispatch(unsetCurrentUser());
        toastOnError(error)
    });
};

export const setCurrentUser=(user,redirectTo)=>dispatch=>{
    localStorage.setItem("user",JSON.stringify(user));
    dispatch({
        type:SET_CURRENT_USER,
        payload:user
    });
    console.log("set user"+redirectTo)
    if(redirectTo!==""){
        dispatch(push(redirectTo))
    }
}
export const setToken=token=>dispatch=>{
    console.log(token)
    setAxiosAuthToken(token)
    localStorage.setItem("token",token)
    dispatch({
        type:SET_TOKEN,
        payload:token
    })
}

export const unsetCurrentUser=()=>dispatch=>{
    setAxiosAuthToken("");
    localStorage.removeItem("token");
    localStorage.removeItem("user")
    dispatch({
        type:UNSET_CURRENT_USER
    });
};

export const logout=()=>dispatch=>{
    axios.post("api/logout/")
    .then(response=>{
        dispatch(unsetCurrentUser());
        dispatch(push("/"))
        toast.success("Logout Successful")
    })
    .catch(err=>{
        dispatch(unsetCurrentUser())
        toastOnError(err);
    })
}