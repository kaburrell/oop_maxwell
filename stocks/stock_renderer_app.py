import stock_model, stock_view

if __name__ == '__main__':

    # analyze stock
    model = stock_model.StockModel('APPL', 159.29, 163.05, 44035531, 22509937)

    # display recommendation
    view = stock_view.StockView()
    render_string = view.render(model)

    print(render_string)
