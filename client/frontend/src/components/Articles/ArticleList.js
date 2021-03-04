import React,{useEffect} from 'react'
import {useSelector,useDispatch} from 'react-redux';
import {getArticles} from './ArticleActions.js';
export default function Article() {
    const dispatch = useDispatch()
    const articles = useSelector(state => state.articles.articles)
    useEffect(()=>{
        dispatch(getArticles())

    },[])
    return (
        <div>
            {
                articles?.map((article,index)=>{
                   return  <div key={index}>
                        {article.title}
                    </div>
                })
            }
        </div>
    )
}
