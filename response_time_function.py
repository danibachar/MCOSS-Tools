def response_time_function(job_type, scale = 1):
    if job_type == "product_page":
        return 0.006 / scale, 0.0#0.22
    if job_type == "user_page":
        return 0.006 / scale, 0.0#0.22
    if job_type == "dashboard":
        return 0.006 / scale, 0.0#0.22
    if job_type == "review":
        return 0.01 / scale, 0.0#0.22
    if job_type == "details":
        return 0.009 / scale, 0.0#0.22
    if job_type == "rating":
        return 0.016 / scale, 0.0# 0.22
    if job_type == "main_db":
        return 0.021 / scale, 0.0#0.22
    if job_type == "image_server":
        return 0.006 / scale, 0.0#0.22
    if job_type == "storage":
        return 0.026 / scale, 0.0

def duration_by(load, type, scale):
    slope, b = response_time_function(type, scale)
    duration_in_seconds = (slope * load + b)
    return duration_in_seconds