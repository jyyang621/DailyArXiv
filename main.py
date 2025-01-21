import sys  
import time  
import pytz  
from datetime import datetime  
import timeout_decorator  
from contextlib import contextmanager  
from utils import get_daily_papers_by_keyword_with_retries, generate_table, back_up_files,\
    restore_files, remove_backups, get_daily_date  

@contextmanager  
def safe_file_operations():  
    try:  
        back_up_files()  
        yield  
    except Exception as e:  
        print(f"Error during file operations: {e}")  
        restore_files()  
        sys.exit(1)  
    finally:  
        remove_backups()  

def read_last_update_date():  
    try:  
        with open("README.md", "r") as f:  
            for line in f:  
                if "Last update:" in line:  
                    return line.split(": ")[1].strip()  
        raise ValueError("No 'Last update:' found in README.md")  
    except Exception as e:  
        print(f"Error reading last update date: {e}")  
        sys.exit(1)  

@timeout_decorator.timeout(300)  # 5分钟超时  
def safe_paper_fetch(keyword, column_names, max_result, link):  
    return get_daily_papers_by_keyword_with_retries(keyword, column_names, max_result, link)  

def exponential_backoff(attempt, base_delay=5):  
    delay = min(base_delay * (2 ** attempt), 60)  # 最大延迟60秒  
    time.sleep(delay)  

def main():  
    beijing_timezone = pytz.timezone('Asia/Shanghai')  
    current_date = datetime.now(beijing_timezone).strftime("%Y-%m-%d")  
    last_update_date = read_last_update_date()  
    
    # if last_update_date == current_date:  
    #     sys.exit("Already updated today!")  

    keywords = ["RAG", "LLM", "SFT", "Fine-tune", "RLHF"]  
    print(keywords)
    max_result = 100  
    issues_result = 15  
    column_names = ["Title", "Link", "Abstract", "Date", "Comment"]  

    with safe_file_operations():  
        with open("README.md", "w") as f_rm, open(".github/ISSUE_TEMPLATE.md", "w") as f_is:  
            # 写入 README.md 头部  
            f_rm.write("# Daily Papers\n")  
            f_rm.write("The project automatically fetches the latest papers from arXiv based on keywords.\n\n")  
            f_rm.write("The subheadings in the README file represent the search keywords.\n\n")  
            f_rm.write("Only the most recent articles for each keyword are retained, up to a maximum of 100 papers.\n\n")  
            f_rm.write("You can click the 'Watch' button to receive daily email notifications.\n\n")  
            f_rm.write(f"Last update: {current_date}\n\n")  

            # 写入 ISSUE_TEMPLATE.md 头部  
            f_is.write("---\n")  
            f_is.write(f"title: Latest {issues_result} Papers - {get_daily_date()}\n")  
            f_is.write("labels: documentation\n")  
            f_is.write("---\n")  
            f_is.write("**Please check the [Github](https://github.com/zezhishao/MTS_Daily_ArXiv) page for a better reading experience and more papers.**\n\n")  

            for i, keyword in enumerate(keywords):  
                try:  
                    print(f"Processing keyword: {keyword}")  
                    link = "AND" if len(keyword.split()) == 1 else "OR"  
                    papers = safe_paper_fetch(keyword, column_names, max_result, link)  
                    
                    if papers is None:  
                        raise ValueError(f"Failed to get papers for keyword: {keyword}")  
                    
                    # 生成并写入表格  
                    rm_table = generate_table(papers)  
                    is_table = generate_table(papers[:issues_result], ignore_keys=["Abstract"])  
                    
                    f_rm.write(f"## {keyword}\n{rm_table}\n\n")  
                    f_is.write(f"## {keyword}\n{is_table}\n\n")  
                    
                    # 在处理最后一个关键词之前添加延迟  
                    if i < len(keywords) - 1:  
                        exponential_backoff(i)  
                        
                except timeout_decorator.TimeoutError:  
                    print(f"Timeout while processing keyword: {keyword}")  
                    raise  
                except Exception as e:  
                    print(f"Error processing keyword {keyword}: {e}")  
                    raise  

if __name__ == "__main__":  
    try:  
        main()  
    except Exception as e:  
        print(f"Program failed: {e}")  
        sys.exit(1)
