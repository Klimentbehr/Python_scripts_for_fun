from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import networkx as nx
import matplotlib.pyplot as plt

# Preset credentials (not secure, for demonstration only)
LINKEDIN_USER = "aug.behr@gmail.com"
LINKEDIN_PASS = "Coolcat25"

def login_to_linkedin(driver):
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    # Log in to LinkedIn
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    # Simulate human typing
    username.send_keys(LINKEDIN_USER)
    time.sleep(1)
    password.send_keys(LINKEDIN_PASS)
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)  # Wait for login to complete

def get_job_count(driver, url):
    # Navigate to the specified URL
    driver.get(url)
    time.sleep(5)  # Wait for page to load completely

    # Look for the job count in the 'My jobs' section
    job_count_element = driver.find_element(By.XPATH, "//a[contains(@href, '/my-items/saved-jobs') and contains(@class, 'mn-my-items__content')]/span")
    job_count = int(job_count_element.text.strip())
    return job_count

def create_flow_chart(applied_jobs_count, in_progress_jobs_count):
    # Create the flow chart
    G = nx.DiGraph()
    G.add_node("Total Applications", count=applied_jobs_count + in_progress_jobs_count)
    G.add_node("Applied Jobs", count=applied_jobs_count)
    G.add_node("In Progress Jobs", count=in_progress_jobs_count)

    G.add_edges_from([
        ("Total Applications", "Applied Jobs", {'weight': applied_jobs_count}),
        ("Total Applications", "In Progress Jobs", {'weight': in_progress_jobs_count})
    ])

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
    edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    plt.title("Job Application Flow Chart")
    plt.show()

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)

    try:
        login_to_linkedin(driver)
        applied_jobs_count = get_job_count(driver, "https://www.linkedin.com/my-items/saved-jobs/?cardType=APPLIED")
        in_progress_jobs_count = get_job_count(driver, "https://www.linkedin.com/my-items/saved-jobs/?cardType=IN_PROGRESS")
        create_flow_chart(applied_jobs_count, in_progress_jobs_count)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
