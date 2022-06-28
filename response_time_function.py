def response_time_function(job_type):
    if job_type == "product_page":
        return 0.006, 0.0#0.22
    if job_type == "user_page":
        return 0.006, 0.0#0.22
    if job_type == "dashboard":
        return 0.006, 0.0#0.22
    if job_type == "review":
        return 0.01, 0.0#0.22
    if job_type == "details":
        return 0.009, 0.0#0.22
    if job_type == "rating":
        return 0.016, 0.0# 0.22
    if job_type == "main_db":
        return 0.021, 0.0#0.22
    if job_type == "image_server":
        return 0.006, 0.0#0.22
    if job_type == "storage":
        return 0.026, 0.0

def duration_by(load, type):
    slope, b = response_time_function(type)
    duration_in_seconds = (slope * load + b)
    return duration_in_seconds