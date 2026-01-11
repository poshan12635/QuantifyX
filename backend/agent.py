
from dotenv import load_dotenv
import os
from typing import Annotated,List,TypedDict
import pandas as pd
from langgraph.graph import START,END
from langgraph.prebuilt import ToolNode,tools_condition
from langchain_groq import ChatGroq
from langchain_core import tools
from demo import pattern_finder,get_bollinger_triggers
from Backtest import BollingerRsi,bollinger_band,MeanReversion,macrossover
from backtesting import Backtest



api_key=os.getenv("api")

model="meta-llama/llama-4-maverick-17b-128e-instruct"

class AgentState(TypedDict):
    stock_ticker: str
    raw_data: List[dict]
    cash:float
    signal_dates1: List[str]  
    signal_dates2:List[str]
    rsi1:List[str]
    rsi2:List[str]
    
    news_report: str
    final_hypothesis: str

@tools
def BollingerRsi(inv,data):
    result=Backtest(BollingerRsi,cash=inv,commission=0)
    return result
    
@tools
def bollinger(data):
    result=get_bollinger_triggers(data)
    return data

def technical_research_node(state:AgentState,data):
    ticker=state["stock_ticker"]
    result1=bollinger.invoke({"data":data})
    result2=volume.invoke({"data":data})
    return{
        result1['date'],
        result2['date']
        
    }
    

    
    
