import math
import numpy as np

points = []


def draw_line_dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    if steps == 0:
        return []
    
    x_increment = dx / steps
    y_increment = dy / steps
    
    x = x1
    y = y1
    
    line_points = [(round(x), round(y))]
    
    for _ in range(int(steps)):
        x += x_increment
        y += y_increment
        line_points.append((round(x), round(y)))
    
    return line_points


def get_translation_matrix(t):
    return np.array([[1., 0., t[0]],
                     [0., 1., t[1]],
                     [0., 0., 1.]])


def translation(v, t):
    if not v:
        return []
    translation_matrix = get_translation_matrix(t)
    v = np.asarray(v, dtype=float)
    v = np.c_[v, np.ones(v.shape[0])]
    v = v.T

    v_translated = np.matmul(translation_matrix, v)
    v_list = v_translated.T[:, :2].tolist()
    
    points.clear()
    # Draw line between transformed points
    for i in range(len(v_list)-1):
        x1, y1 = v_list[i]
        x2, y2 = v_list[i+1]
        line_points = draw_line_dda(x1, y1, x2, y2)
        points.extend(line_points)
    
    return points


def get_rotation_matrix(angle):
    theta = math.radians(angle)
    c = math.cos(theta)
    s = math.sin(theta)
    return np.array([[c, -s, 0],
                     [s, c, 0],
                     [0, 0, 1]])


def rotation(v, angle, pivot=None):
    if not v:
        return []
    
    v = np.asarray(v, dtype=float)
    
    if pivot is None:
        # Use centroid as pivot point
        pivot = np.mean(v, axis=0)
    
    # Translate to origin
    v_centered = v - pivot
    
    # Apply rotation
    rotation_matrix = get_rotation_matrix(angle)
    v_centered = np.c_[v_centered, np.ones(v_centered.shape[0])]
    v_centered = v_centered.T
    v_rotated = np.matmul(rotation_matrix, v_centered)
    
    # Translate back
    v_list = (v_rotated.T[:, :2] + pivot).tolist()
    
    points.clear()
    # Draw line between transformed points
    for i in range(len(v_list)-1):
        x1, y1 = v_list[i]
        x2, y2 = v_list[i+1]
        line_points = draw_line_dda(x1, y1, x2, y2)
        points.extend(line_points)
    
    return points


def get_reflection_matrix(axis='x'):
    if axis.lower() == 'x':
        return np.array([[1., 0., 0.],
                        [0., -1., 0.],
                        [0., 0., 1.]])
    elif axis.lower() == 'y':
        return np.array([[-1., 0., 0.],
                        [0., 1., 0.],
                        [0., 0., 1.]])
    else:
        raise ValueError("Axis must be 'x' or 'y'")


def reflection(v, axis='x'):
    if not v:
        return []
    reflection_matrix = get_reflection_matrix(axis)
    v = np.asarray(v, dtype=float)
    v = np.c_[v, np.ones(v.shape[0])]
    v = v.T
    
    v_reflected = np.matmul(reflection_matrix, v)
    v_list = v_reflected.T[:, :2].tolist()
    
    points.clear()
    # Draw line between transformed points
    for i in range(len(v_list)-1):
        x1, y1 = v_list[i]
        x2, y2 = v_list[i+1]
        line_points = draw_line_dda(x1, y1, x2, y2)
        points.extend(line_points)
    
    return points


def get_scaling_matrix(sx, sy):
    return np.array([[sx, 0., 0.],
                     [0., sy, 0.],
                     [0., 0., 1.]])


def scaling(v, sx, sy):
    if not v:
        return []
    scaling_matrix = get_scaling_matrix(sx, sy)
    v = np.asarray(v, dtype=float)
    v = np.c_[v, np.ones(v.shape[0])]
    v = v.T
    
    v_scaled = np.matmul(scaling_matrix, v)
    v_list = v_scaled.T[:, :2].tolist()
    
    points.clear()
    # Draw line between transformed points
    for i in range(len(v_list)-1):
        x1, y1 = v_list[i]
        x2, y2 = v_list[i+1]
        line_points = draw_line_dda(x1, y1, x2, y2)
        points.extend(line_points)
    
    return points


def get_shearing_matrix(shx=0, shy=0):
    return np.array([[1., shx, 0.],
                     [shy, 1., 0.],
                     [0., 0., 1.]])


def shearing(v, shx=0, shy=0):
    if not v:
        return []
    shearing_matrix = get_shearing_matrix(shx, shy)
    v = np.asarray(v, dtype=float)
    v = np.c_[v, np.ones(v.shape[0])]
    v = v.T
    
    v_sheared = np.matmul(shearing_matrix, v)
    v_list = v_sheared.T[:, :2].tolist()
    
    points.clear()
    # Draw line between transformed points
    for i in range(len(v_list)-1):
        x1, y1 = v_list[i]
        x2, y2 = v_list[i+1]
        line_points = draw_line_dda(x1, y1, x2, y2)
        points.extend(line_points)
    
    return points