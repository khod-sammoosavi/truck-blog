from . import Admin
from settings.static_configs import admin_settings_pages
from flask import render_template, redirect, request, flash


def views():
    @Admin.route("/")
    def index():
        return redirect("/admin/pages")

    list_of_pages = {}
    admin_pages = admin_settings_pages

    @Admin.route("/pages", methods=["POST", "GET"])
    def pages():
        current_url = request.path
        page_name = None
        page_slug = None
        if request.method == "POST":
            page_name = request.form["name"]
            page_slug = request.form["slug"]
            if page_slug != "" and page_slug != "":
                list_of_pages[page_name] = page_slug
            else:
                flash("Name or Slug is None")

        return render_template("pages.html", current_url=current_url,
                               pages=admin_pages, list_of_pages=list_of_pages)

    @Admin.route("/delete_all_pages", methods=["POST", "GET"])
    def delete_all_pages():
        list_of_pages.clear()
        return redirect("/admin/pages")

    @Admin.route("/pages/page/<page_slug>", methods=["GET", "POST"])
    def page(page_slug):
        this_page = list(list_of_pages.keys())[list(list_of_pages.values()).index(page_slug)]
        new_page_name = None
        new_page_slug = None
        if request.method == "POST":
            new_page_name = request.form["new-name"]
            new_page_slug = request.form["new-slug"]
            if new_page_slug != "" and new_page_slug != "":
                list_of_pages[new_page_name] = new_page_slug
            else:
                flash("Name or Slug is None")

        return render_template("page.html", pages=admin_pages,
                               list_of_pages=list_of_pages,
                               page_slug=page_slug, page_name=this_page)

    @Admin.route("/pages/page/<page_slug>/delete_this_page", methods=["POST", "GET"])
    def delete_this_page(page_slug):
        this_page = list(list_of_pages.keys())[list(list_of_pages.values()).index(page_slug)]
        list_of_pages.pop(this_page)
        return redirect("/admin/pages")

    return Admin
